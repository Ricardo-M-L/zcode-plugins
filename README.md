# ZCode Plugins Marketplace

[中文文档](./README_CN.md)

The official plugins marketplace for [ZCode](https://zcode.z.ai), featuring plugins maintained by ZCode and contributions from the community.

Use this repository to browse available plugins, install the marketplace in compatible clients, or propose a new plugin through a GitHub pull request.

## Documentation

- [Contributing guide](./CONTRIBUTING.md) ([中文](./CONTRIBUTING_CN.md))
- [Distribution format](./docs/distribution.md) ([中文](./docs/distribution_CN.md))
- [Plugin development tutorial](./docs/PLUGIN_DEVELOPMENT.md) ([中文](./docs/PLUGIN_DEVELOPMENT_CN.md))

## Available Plugins

| Plugin | Category | Description |
| --- | --- | --- |
| [**cloudbase-skills**](./plugins/cloudbase-skills) | `developer-tools` | CloudBase development skills and MCP integration for Web, Mini Program, database, cloud functions, CloudRun, storage, and AI projects. |
| [**mimosa**](./plugins/mimosa) | `developer-tools` | Local-first security guardrails with pre-write hooks, review and Git gates, security commands, and optional sealed deep scans. |
| [**github**](./plugins/github) | `developer-tools` | GitHub CLI workflows for commits, pull requests, issues, releases, Actions, repositories, and Codespaces. |
| [**gitlab**](./plugins/gitlab) | `developer-tools` | GitLab CLI workflows for merge requests, issues, CI/CD, repositories, releases, and API operations, including self-managed instances. |
| [**alibaba-cloud-cli**](./plugins/alibaba-cloud-cli) | `developer-tools` | Alibaba Cloud CLI workflows for credential setup, profile checks, and safe cloud resource operations. |
| [**hyper3d-rodin**](./plugins/hyper3d-rodin) | `developer-tools` | Generate and split 3D models with Hyper3D Rodin Gen-2.5 and BANG. |
| [**video-agent-kit**](./plugins/video-agent-kit) | `productivity` | Automated video editing with transcription, frame analysis, timeline editing, preview rendering, QC, and TTS. |
| [**video2code**](./plugins/video2code) | `productivity` | Replicate a webpage from a screen recording or URL: record with the built-in WebView, observe frames, scaffold a React app, and verify against the source. |
| [**lark-cli**](./plugins/lark-cli) | `productivity` | Lark CLI workflows for docs, sheets, Base, calendar, messaging, and other SaaS resources with guided setup and OAuth login. |
| [**tencent-meeting-cli**](./plugins/tencent-meeting-cli) | `productivity` | Tencent Meeting CLI workflows for OAuth setup, meeting management, recordings, and attendee reports. |
| [**dingtalk-cli**](./plugins/dingtalk-cli) | `productivity` | DingTalk Workspace CLI workflows with OAuth/device authorization, profile checks, and optional upstream Skills. |
| [**wecom-cli**](./plugins/wecom-cli) | `productivity` | WeCom CLI workflows for messages, docs, sheets, mail, calendar, meetings, contacts, and todos with QR authentication. |
| [**obsidian**](./plugins/obsidian) | `productivity` | Obsidian authoring, vault automation, web extraction, templates, Mermaid, Excalidraw, and Canvas workflows. |

### Finance plugins

Fourteen `finance` plugins cover the sell side, the buy side, corporate banking, corporate
finance, and financial-data access. Ten workflow plugins pair a routing agent with domain
skills; four connector plugins expose iFinD, Wind, Tianyancha, SEC, web, and news data through
MCP services. Remote services authenticate through the ZCode host, so there is no data-vendor
account to configure. `accounting-and-reporting` works entirely from your own ledger.

| Plugin | Focus | What it does |
| --- | --- | --- |
| [**write-research**](./plugins/write-research) | Equity research | Earnings work, sector and thematic reports, comps, DCF / LBO / three-statement models, morning notes, integrated reports. |
| [**read-macro**](./plugins/read-macro) | Macro & strategy | Macro state dashboard, index valuation percentiles, cross-asset views, policy and industrial-plan tracking. |
| [**assess-credit**](./plugins/assess-credit) | Fixed income & credit | Bond profiles with valuation and risk metrics, issuer credit assessment, curve and spread analysis, credit watchlists. |
| [**pick-funds**](./plugins/pick-funds) | Fund research | Multi-criteria fund screening, fund and manager profiles, holdings and style analysis, shortlist monitoring. |
| [**watch-positions**](./plugins/watch-positions) | Position monitoring | Persistent watchlists, after-close recaps with move attribution, event alerts, intraday view. |
| [**model-deals**](./plugins/model-deals) | Deal modeling | Accretion/dilution, sources and uses with pro-forma capital structure, precedent transactions, capital-raise dilution. |
| [**vet-companies**](./plugins/vet-companies) | Company due diligence | Structured DD reports, related-party and supply-chain mapping, risk-record screens. |
| [**find-clients**](./plugins/find-clients) | Corporate client acquisition | Prospect screening, park and cluster maps, business-opportunity signals, client portraits. |
| [**run-fpa**](./plugins/run-fpa) | Corporate FP&A | Management reporting, rolling cash and P&L forecasts, budget variance attribution, scenarios, peer benchmarking. |
| [**accounting-and-reporting**](./plugins/accounting-and-reporting) | Accounting & reporting | Month-end close review, ledger reconciliation to root cause, account mapping, statutory statements, three-statement tie-out. |
| [**hexin**](./plugins/hexin) | iFinD market data | Stock, global stock, index, fund, and bond data through MCP services. |
| [**wind**](./plugins/wind) | Wind market data | Stock, global stock, index, fund, bond, macroeconomic, announcement, and research data through MCP services. |
| [**tianyancha**](./plugins/tianyancha) | Company information | Tianyancha company-information queries through an MCP service. |
| [**finance-search**](./plugins/finance-search) | Financial search | SEC EDGAR filing search plus financial web and news search through MCP services. |

## Marketplace categories

The `category` field in [`marketplace.json`](./marketplace.json) keeps discovery consistent:

| Category | Use it for | Current plugins |
| --- | --- | --- |
| `developer-tools` | Development, code quality, Git, CI, and engineering workflows | `cloudbase-skills`, `mimosa`, `github`, `gitlab`, `alibaba-cloud-cli`, `hyper3d-rodin` |
| `productivity` | Planning, knowledge work, and personal workflow automation | `video-agent-kit`, `video2code`, `lark-cli`, `tencent-meeting-cli`, `dingtalk-cli`, `wecom-cli`, `obsidian` |
| `utilities` | General-purpose helpers that do not fit another category | — |
| `finance` | Finance-domain workflows: markets, accounting, risk, and fintech integrations | `write-research`, `read-macro`, `assess-credit`, `pick-funds`, `watch-positions`, `model-deals`, `vet-companies`, `find-clients`, `run-fpa`, `accounting-and-reporting`, `hexin`, `wind`, `tianyancha`, `finance-search` |
| `guides` | Documentation, learning, and reference-only plugins | — |
| `template` | Copyable scaffolding for creating a plugin | — |
| `other` | A plugin that does not fit the categories above | — |

## Installation

### In ZCode

ZCode includes the official marketplace. Open the plugin manager, choose a plugin, and install it directly.

## Community

Have a question about a plugin, or building one of your own? Join the ZCode plugin developers on Discord — that is where we answer questions, share work in progress, and announce marketplace releases.

<a href="https://discord.gg/rhdRRNPqhh">
  <img src="./docs/images/community-discord.png" alt="Join the ZCode plugin developer community on Discord" width="360">
</a>

Developers in mainland China can join our Feishu group instead — see the [中文文档](./README_CN.md#社区).

## Contributing

Community contributions are welcome:

1. Copy [`plugins/example-plugin/`](./plugins/example-plugin) to `plugins/<your-plugin-name>/` and follow the [development tutorial](./docs/PLUGIN_DEVELOPMENT.md).
2. Register the plugin in [`marketplace.json`](./marketplace.json), including its category.
3. Provide equivalent English and Chinese documentation.
4. Run the local checks:

```shell
python3 scripts/validate.py
python3 scripts/build_dist.py
```

5. Open a GitHub pull request and complete the contribution checklist.

Maintainers review submissions for quality, security, compatibility, and licensing. Accepted changes are published through the official release process, and the pull request receives a status update when publication is complete.

See the [contributing guide](./CONTRIBUTING.md) for the complete requirements.

## License

Apache License 2.0
