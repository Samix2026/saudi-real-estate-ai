# saudi-real-estate-ai

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: Arabic](https://img.shields.io/badge/Language-Arabic-green.svg)](README.ar.md)
[![JSON Schema](https://img.shields.io/badge/JSON-Schema-blue.svg)](schemas/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](scripts/)

**AI-ready knowledge infrastructure for Saudi Arabia's real estate ecosystem.**

---

## Overview

`saudi-real-estate-ai` is a structured, open-source knowledge base of Saudi real estate regulations, platforms, authorities, contracts, and terminology — designed for AI agents, developers, and researchers building real estate applications for the Saudi market.

The repository organises verified regulatory data from official Saudi sources (REGA, ejar, wafi, sakani) into machine-readable JSON datasets, JSON Schema definitions, bilingual system prompts, and documented source citations. Every dataset is bilingual (Arabic / English) and validated against a schema, making it drop-in ready for RAG pipelines, MCP servers, chatbots, and AI agents that need grounded, authoritative Saudi real estate knowledge.

---

## Scope

| Area | Detail |
|---|---|
| Regulations | REGA real estate law, rental regulations, off-plan sales rules |
| Platforms | ejar (rental contracts), wafi (off-plan), sakani (housing programs) |
| Authorities | REGA, Ministry of Municipalities and Housing, municipal bodies |
| Contracts | Rental, sale, off-plan, commercial lease |
| Terminology | Bilingual glossary of Saudi real estate terms (AR / EN) |
| AI Artifacts | System prompts, example Q&A pairs, JSON schemas |

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

## Use Cases

- Build Saudi real estate chatbots grounded in verified regulatory data
- Power AI agents with structured, citable knowledge about Saudi property law
- Validate rental contracts against Saudi law and ejar platform requirements
- Check broker and developer compliance against REGA licensing rules
- Analyse off-plan purchase risks using wafi program data
- Support foreign investor onboarding with bilingual market entry guidance
- Seed RAG (Retrieval-Augmented Generation) pipelines with Saudi domain knowledge
- Train or fine-tune language models on Saudi real estate Arabic terminology

---

## Repository Structure

```
saudi-real-estate-ai/
├── README.md
├── README.ar.md
├── ROADMAP.md
├── CLAUDE.md
├── LICENSE
├── sources/
│   ├── index.md
│   ├── rega.md
│   ├── ejar.md
│   ├── wafi.md
│   └── sakani.md
├── data/
│   ├── platforms.ar.json
│   ├── platforms.en.json
│   ├── authorities.ar.json
│   ├── contract-types.ar.json
│   ├── real-estate-terms.ar.json
│   └── market-concepts.ar.json
├── schemas/
│   ├── platforms.schema.json
│   ├── authorities.schema.json
│   └── contract-types.schema.json
├── prompts/
│   ├── rental-contract-review.md
│   ├── broker-compliance-check.md
│   ├── off-plan-sale-check.md
│   └── investor-market-entry.md
├── examples/
│   ├── tenant-question.ar.md
│   ├── landlord-question.ar.md
│   └── investor-question.en.md
└── scripts/
    ├── validate-data.py
    └── query-dataset.py
```

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/saudi-real-estate-ai.git
cd saudi-real-estate-ai

# Install the validation dependency
pip install jsonschema

# Validate all datasets against their schemas
python scripts/validate-data.py
```

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full phased plan, including MCP integration, Arabic embeddings, and community dataset expansion.

---

## Contributing

Contributions are welcome. Please open an issue before submitting a pull request that adds new datasets or modifies existing schemas. All contributions must cite an official Saudi authority source and pass schema validation (`python scripts/validate-data.py`). See [CLAUDE.md](CLAUDE.md) for AI agent contribution guidelines.

---

## Disclaimer

> **Warning:** This repository is for informational and AI training purposes only. It does not constitute legal or financial advice. Regulations and platform policies change — always verify current requirements through official Saudi authorities (REGA, ejar, wafi, sakani) and consult licensed Saudi real estate professionals before making any legal or financial decisions.

---

## License

[MIT](LICENSE) — 2025 saudi-real-estate-ai Contributors
