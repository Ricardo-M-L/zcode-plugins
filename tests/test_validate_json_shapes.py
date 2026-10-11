"""Malformed-but-valid JSON should produce actionable validation errors."""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = REPOSITORY_ROOT / "scripts" / "validate.py"
    spec = importlib.util.spec_from_file_location("validate_json_shapes", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


validate = load_validator()


class JsonShapeValidationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="validate-json-shapes-")
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)
        self.plugin_dir = self.root / "plugins" / "valid-plugin"
        (self.plugin_dir / ".zcode-plugin").mkdir(parents=True)
        self.entry = {
            "name": "valid-plugin",
            "source": "./plugins/valid-plugin",
            "description": "A valid plugin",
            "description_i18n": {
                "en": "A valid plugin",
                "zh-CN": "一个有效插件",
            },
            "version": "1.0.0",
            "category": "utilities",
        }
        self.marketplace = {
            "name": "test-marketplace",
            "owner": {"name": "Test"},
            "description": "Test marketplace",
            "description_i18n": {
                "en": "Test marketplace",
                "zh-CN": "测试市场",
            },
            "plugins": [self.entry],
        }
        self._write_json(
            self.plugin_dir / ".zcode-plugin" / "plugin.json",
            {
                "name": self.entry["name"],
                "description": self.entry["description"],
                "description_i18n": self.entry["description_i18n"],
                "version": self.entry["version"],
            },
        )

    @staticmethod
    def _write_json(path: Path, value: object) -> None:
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def _run(self, marketplace: object) -> tuple[int, str]:
        self._write_json(self.root / "marketplace.json", marketplace)
        old_root = validate.ROOT
        old_plugins_root = validate.PLUGINS_ROOT
        old_errors = validate.errors
        validate.ROOT = self.root
        validate.PLUGINS_ROOT = (self.root / "plugins").resolve()
        validate.errors = []
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                result = validate.main()
        finally:
            validate.ROOT = old_root
            validate.PLUGINS_ROOT = old_plugins_root
            validate.errors = old_errors
        return result, output.getvalue()

    def test_marketplace_top_level_must_be_an_object(self) -> None:
        for value in ([], "marketplace", 42, None):
            with self.subTest(value=value):
                result, output = self._run(value)
                self.assertEqual(result, 1)
                self.assertIn(
                    "marketplace.json: top-level JSON value must be an object",
                    output,
                )

    def test_each_plugin_entry_must_be_an_object(self) -> None:
        marketplace = copy.deepcopy(self.marketplace)
        marketplace["plugins"] = [None, [], "plugin", 42, self.entry]

        result, output = self._run(marketplace)

        self.assertEqual(result, 1)
        for index in range(4):
            self.assertIn(
                f"marketplace.json plugins[{index}]: must be an object",
                output,
            )

    def test_manifest_top_level_must_be_an_object(self) -> None:
        manifest_path = self.plugin_dir / ".zcode-plugin" / "plugin.json"
        for value in ([], "manifest", 42, None):
            with self.subTest(value=value):
                self._write_json(manifest_path, value)
                result, output = self._run(self.marketplace)
                self.assertEqual(result, 1)
                self.assertIn(
                    "plugins/valid-plugin/.zcode-plugin/plugin.json: "
                    "top-level JSON value must be an object",
                    output,
                )

    def test_scalar_field_types_fail_without_tracebacks(self) -> None:
        cases = {
            "name": (42, "'name' must be a non-empty string"),
            "version": ([], "'version' must be a non-empty string"),
            "category": (["utilities"], "not in allowed set"),
        }
        for field, (value, message) in cases.items():
            with self.subTest(field=field):
                marketplace = copy.deepcopy(self.marketplace)
                marketplace["plugins"][0][field] = value
                result, output = self._run(marketplace)
                self.assertEqual(result, 1)
                self.assertIn(message, output)


if __name__ == "__main__":
    unittest.main()
