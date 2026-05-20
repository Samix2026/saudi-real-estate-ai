# CLAUDE.md — AI Agent Guidelines for saudi-real-estate-ai

This file defines the conventions, standards, and behavioural rules for AI agents (Claude Code, Copilot, GPT, and similar) working inside this repository. All agents must read this file before modifying any content.

---

## Repository Purpose

`saudi-real-estate-ai` is a structured knowledge base for Saudi Arabia's real estate sector, designed primarily for AI agent consumption. It contains verified regulatory data, platform information, contract types, terminology, and system prompts — all sourced from official Saudi authorities. The goal is to provide developers and AI systems with a grounded, bilingual, schema-validated foundation for building real estate applications that comply with Saudi law and best practices. Every dataset entry must be traceable to an official source; nothing should be inferred or generated without a citation.

---

## Conventions

- All data files live in `data/` and **must validate** against their corresponding schema in `schemas/` before being committed. Run `python scripts/validate-data.py` to check.
- Sources are documented in `sources/` with full citations to official URLs, publication dates where known, and a brief scope description. Never add a data entry without first confirming its source is documented in `sources/`.
- Files in `prompts/` are **system-prompt templates**, not user messages. They are designed to be inserted as the `system` role in a chat completion call. Do not write them in first-person user voice.
- Arabic content must use **Modern Standard Arabic (MSA)** with authentic Saudi real estate terminology as used by REGA, ejar, wafi, and sakani. Do not translate technical terms loosely — use the exact Arabic phrasing that appears in official documents.
- Bilingual files (`.ar.json` / `.en.json`) must remain in sync. When you update one, update the other in the same commit.

---

## Dataset Standards

All JSON entries in `data/` must conform to the following field requirements:

| Field | Type | Requirement |
|---|---|---|
| `id` | string | snake_case, unique within the file, no spaces or hyphens |
| `name_ar` | string | Official Arabic name, as used by the relevant authority |
| `name_en` | string | Official English name or accepted translation |
| `description_ar` | string | Clear Arabic description, 1–4 sentences |
| `description_en` | string | Clear English description, 1–4 sentences |
| `source_url` | string | Direct URL to the official page confirming this entry |
| `last_verified` | string | ISO 8601 date (`YYYY-MM-DD`) of last human or agent verification |

Additional rules:
- IDs must be `snake_case` (e.g., `rental_contract`, `off_plan_sale`, `rega_license`).
- Dates must be ISO 8601 format: `YYYY-MM-DD`.
- Monetary values must be denominated in **SAR (Saudi Riyal)** unless explicitly noted otherwise.
- Do not use placeholders (`TBD`, `N/A`, `unknown`) in required fields — omit optional fields instead.
- Arrays must not contain duplicate entries.

---

## AI Behaviour Rules

These rules apply to any AI agent reading, writing, or modifying files in this repository:

1. **Preserve official Arabic terminology.** Use the exact Arabic phrasing that appears in official REGA, ejar, wafi, and sakani publications. Do not paraphrase, simplify, or back-translate from English when the official Arabic term is known.

2. **Never hallucinate regulations.** Only include information that is directly traceable to an official Saudi government source. If you cannot find a `source_url` for a claim, do not add it. Mark uncertain entries with a `needs_verification: true` flag rather than guessing.

3. **Always cite `source_url`.** Every new entry you add to a data file must include a `source_url` pointing to an official page (rega.gov.sa, ejar.sa, wafi.rega.gov.sa, sakani.com.sa, or moh.gov.sa). Links to third-party summaries are not acceptable as the primary source.

4. **Maintain bilingual consistency.** `name_ar` and `name_en` must refer to the same concept with equivalent meaning. A mismatch between the Arabic and English descriptions is a validation error.

5. **Run validation before committing data changes.** Always execute `python scripts/validate-data.py` after editing any file in `data/` or `schemas/`. Do not commit if validation fails.

6. **Do not modify schemas without review.** Changes to files in `schemas/` affect all existing data validation. Open an issue or leave a comment in the PR before altering a schema.

7. **Prompt files are templates, not answers.** When editing files in `prompts/`, write in the voice of instructions given to an AI assistant, not in the voice of a user asking a question or an assistant answering one.

8. **Do not include legal conclusions.** Data files and prompts may describe what Saudi law or a platform requires, but must not assert that a specific transaction is legal, compliant, or advisable. Always include the disclaimer below in any generated content.

---

## Priority Sources

When multiple sources conflict, use this ranking to determine which to trust:

1. **REGA** — [rega.gov.sa](https://www.rega.gov.sa) — Primary regulator for all real estate activity in Saudi Arabia
2. **ejar** — [ejar.sa](https://www.ejar.sa) — Official rental contract platform; authoritative for rental law and contract requirements
3. **wafi** — [wafi.rega.gov.sa](https://wafi.rega.gov.sa) — Official off-plan sales platform; authoritative for developer and buyer obligations
4. **sakani** — [sakani.com.sa](https://www.sakani.com.sa) — National housing program; authoritative for citizen housing eligibility and products
5. **Ministry of Municipalities and Housing** — [moh.gov.sa](https://www.moh.gov.sa) — Higher-level policy and housing strategy

If a lower-priority source contradicts a higher-priority source, trust the higher-priority source and flag the discrepancy with a `conflict_note` field in the entry.

---

## Disclaimers to Include in Generated Content

Any content generated or summarised from this repository — whether a prompt response, a data export, or documentation — must include the following disclaimer, adapted to the language of the content:

**English:**
> This content is for informational and AI training purposes only. It does not constitute legal or financial advice. Always verify through official Saudi authorities (REGA, ejar, wafi, sakani) and consult licensed Saudi real estate professionals before making any legal or financial decisions.

**Arabic:**
> هذا المحتوى لأغراض معلوماتية وتدريب أنظمة الذكاء الاصطناعي فقط، ولا يُعدّ استشارةً قانونية أو مالية. تحقق دائمًا من المتطلبات الحالية عبر الجهات السعودية الرسمية (هيئة العقار، إيجار، وافي، سكني) واستشر متخصصين عقاريين سعوديين مرخَّصين قبل اتخاذ أي قرارات قانونية أو مالية.
