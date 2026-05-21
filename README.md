# saudi-real-estate-ai

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: Arabic](https://img.shields.io/badge/Language-Arabic-green.svg)](README.ar.md)
[![JSON Schema](https://img.shields.io/badge/JSON-Schema-blue.svg)](schemas/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](scripts/)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple.svg)](mcp/)

**AI-ready knowledge infrastructure for Saudi Arabia's real estate ecosystem.**

---

## Project Status

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Foundation — repository structure, sources, CLAUDE.md | ✅ Complete |
| Phase 2 | Datasets — 12 validated JSON datasets, 12 schemas, 83 terms | ✅ Complete |
| Phase 3 | AI Prompts — 5 system prompts, 20 Q&A examples, usage guide | ✅ Complete |
| Phase 4 | MCP Server — 8 tools via stdio, bilingual README | ✅ Complete |
| Phase 5 | Arabic Embeddings — chunked index, semantic search | ⚪ Planned |

---

## Overview

`saudi-real-estate-ai` is a structured, open-source knowledge base of Saudi real estate regulations, platforms, authorities, contracts, and terminology — designed for AI agents, developers, and researchers building real estate applications for the Saudi market.

The repository organises verified regulatory data from official Saudi sources (REGA, ejar, wafi, sakani) into machine-readable JSON datasets, JSON Schema definitions, bilingual system prompts, example Q&A pairs, and a ready-to-run MCP server. Every dataset is bilingual (Arabic / English) and validated against a schema, making it drop-in ready for RAG pipelines, MCP servers, chatbots, and AI agents that need grounded, authoritative Saudi real estate knowledge.

---

## Scope

| Area | Detail |
|---|---|
| Regulations | REGA real estate law, rental regulations, off-plan sales rules |
| Platforms | ejar (rental contracts), wafi (off-plan), sakani (housing programs) |
| Authorities | REGA, Ministry of Municipalities and Housing, municipal bodies |
| Contracts | Rental, sale, off-plan, commercial lease (8 contract types) |
| Terminology | Bilingual glossary of 83 Saudi real estate terms (AR / EN) |
| Property Types | 15 property types with legal definitions, deed types, and ownership restrictions |
| Saudi Building Code | SBC codes (201–801), buyer rights, developer obligations |
| REITs | CMA regulatory framework for REITs listed on Tadawul |
| Housing Programs | 7 national programs: Sakani, REDF, NHC, ROSHN, rental subsidy, and more |
| Property Coding | National Address, REDS title registration, land parcel identification |
| System Prompts | 5 audience-specific prompts: tenant, owner, investor, broker, developer |
| MCP Tools | 8 callable tools via stdio for Claude Desktop and MCP-compatible agents |

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Samix2026/saudi-real-estate-ai.git
cd saudi-real-estate-ai

# Install validation dependency
pip install jsonschema

# Validate all 12 datasets
python3 scripts/validate-data.py
```

---

## MCP Integration

Connect the knowledge base directly to Claude Desktop as callable tools.

**1. Install the MCP dependency:**

```bash
pip install mcp>=1.0.0
```

**2. Add to your Claude Desktop configuration:**

macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "saudi-real-estate-ai": {
      "command": "python3",
      "args": ["/absolute/path/to/saudi-real-estate-ai/mcp/server.py"],
      "env": {}
    }
  }
}
```

**3. Restart Claude Desktop.** The 8 tools will appear in the tool selector:

| Tool | Description |
|---|---|
| `search_terms` | Search bilingual glossary (83 terms) |
| `get_property_type` | Property definitions, deed types, ownership rules |
| `check_broker_requirements` | REGA broker licensing and ethics |
| `get_housing_programs` | Sakani, REDF, NHC, ROSHN, and more |
| `get_reits_framework` | CMA REIT rules and Tadawul requirements |
| `get_building_code` | Saudi Building Code (SBC) requirements |
| `get_foreign_investor_rules` | Foreign ownership rules by nationality |
| `get_property_coding` | National Address, REDS, land parcel systems |

See [`mcp/README.md`](mcp/README.md) for full setup instructions and example calls.

---

## Official Sources

| Authority | Platform | URL |
|---|---|---|
| الهيئة العامة للعقار (REGA) | General Real Estate Authority | [rega.gov.sa](https://www.rega.gov.sa) |
| منصة إيجار | Ejar Rental Platform | [ejar.sa](https://www.ejar.sa) |
| منصة وافي | Wafi Off-Plan Platform | [wafi.rega.gov.sa](https://wafi.rega.gov.sa) |
| برنامج سكني | Sakani Housing Program | [sakani.com.sa](https://www.sakani.com.sa) |
| وزارة البلديات والإسكان | Ministry of Municipalities and Housing | [moh.gov.sa](https://www.moh.gov.sa) |

---

## Repository Structure

```
saudi-real-estate-ai/
├── README.md
├── README.ar.md
├── ROADMAP.md
├── CLAUDE.md
├── LICENSE
├── data/                          # 12 validated JSON datasets
│   ├── platforms.ar.json
│   ├── platforms.en.json
│   ├── authorities.ar.json
│   ├── contract-types.ar.json
│   ├── real-estate-terms.ar.json  # 83 bilingual terms
│   ├── market-concepts.ar.json
│   ├── broker-requirements.ar.json
│   ├── foreign-investor.ar.json
│   ├── property-types.ar.json     # 15 property types
│   ├── saudi-building-code.ar.json
│   ├── reits-framework.ar.json
│   ├── housing-programs.ar.json   # 7 national programs
│   └── property-coding.ar.json
├── schemas/                       # 12 JSON Schema draft-07 files
├── prompts/                       # System prompt templates
│   ├── investor-market-entry.md   # Foreign investor guide
│   └── system-prompts/
│       ├── tenant.md
│       ├── owner.md
│       ├── investor.md
│       ├── broker.md
│       └── developer.md
├── examples/
│   └── qa-by-audience.ar.md       # 20 Q&A pairs (5 audiences)
├── docs/
│   └── usage-guide.md             # RAG, system prompt, and MCP patterns
├── mcp/                           # MCP server (Phase 4)
│   ├── server.py                  # stdio transport, 8 tools
│   ├── tools.py                   # tool implementations
│   ├── requirements.txt
│   └── README.md
├── sources/
│   ├── index.md
│   ├── rega.md
│   ├── ejar.md
│   ├── wafi.md
│   └── sakani.md
└── scripts/
    └── validate-data.py
```

---

## Use Cases

- Build Saudi real estate chatbots grounded in verified regulatory data
- Power AI agents with structured, citable knowledge about Saudi property law
- Validate rental contracts against Saudi law and ejar platform requirements
- Check broker and developer compliance against REGA licensing rules
- Analyse off-plan purchase risks using wafi program data
- Support foreign investor onboarding with bilingual market entry guidance
- Seed RAG pipelines with Saudi domain knowledge
- Use the MCP server to connect Claude Desktop directly to all datasets
- Guide foreign investors through nationality-differentiated ownership pathways using `data/foreign-investor.ar.json`
- Build tenant rights advisors explaining Rental Law obligations and ejar dispute procedures

---

## Contributing

Contributions are welcome. Please open an issue before submitting a pull request that adds new datasets or modifies existing schemas. All contributions must cite an official Saudi authority source and pass schema validation (`python3 scripts/validate-data.py`). See [CLAUDE.md](CLAUDE.md) for AI agent contribution guidelines.

---

## Disclaimer

> **Warning:** This repository is for informational and AI training purposes only. It does not constitute legal or financial advice. Regulations and platform policies change — always verify current requirements through official Saudi authorities (REGA, ejar, wafi, sakani) and consult licensed Saudi real estate professionals before making any legal or financial decisions.

---

## License

[MIT](LICENSE) — 2025 saudi-real-estate-ai Contributors
