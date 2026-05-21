# Roadmap

This roadmap outlines the phased development of `saudi-real-estate-ai` from foundational structure through to a fully community-driven ecosystem with semantic search capabilities.

---

## Phase 1 — Foundation

**Status:** ✅ مكتملة  
**Timeline:** Q2 2025

Establish the repository structure and core documentation so contributors and AI agents have a reliable, well-cited starting point.

- Set up the full repository directory structure (`data/`, `schemas/`, `prompts/`, `sources/`, `scripts/`, `examples/`)
- Write English and Arabic README files with official source citations
- Document all five priority sources in `sources/` with URLs, scope, and reliability notes
- Add `CLAUDE.md` with AI agent conventions and dataset standards
- Define the MIT license and initial contribution guidelines
- Publish the bilingual `ROADMAP.md` and project overview

---

## Phase 2 — Structured Datasets

**Status:** ✅ مكتملة  
**Timeline:** Q2–Q3 2026

Build the core machine-readable knowledge base covering platforms, authorities, contract types, terminology, and market concepts.

- Publish `data/platforms.ar.json` and `data/platforms.en.json` with entries for ejar, wafi, and sakani
- Publish `data/authorities.ar.json` covering REGA, Ministry of Municipalities and Housing, and key municipal bodies
- Publish `data/contract-types.ar.json` covering rental, sale, off-plan, and commercial lease contract types
- Publish `data/real-estate-terms.ar.json` with a bilingual glossary of 50+ Saudi real estate terms
- Publish `data/market-concepts.ar.json` covering Vision 2030 housing targets, REGA licensing tiers, and market structure
- Write JSON Schema files for all datasets (`schemas/platforms.schema.json`, `schemas/authorities.schema.json`, `schemas/contract-types.schema.json`)
- Implement and test `scripts/validate-data.py` against all schemas

---

## Phase 3 — AI Prompts and Examples

**Status:** ✅ مكتملة  
**Timeline:** Q3 2026

Create reusable AI system prompts and bilingual example interactions that developers can integrate directly into chatbots and AI agents.

- Write `prompts/rental-contract-review.md` — a system prompt for reviewing Saudi rental contracts against ejar requirements
- Write `prompts/broker-compliance-check.md` — a system prompt for verifying REGA broker licensing and obligations
- Write `prompts/off-plan-sale-check.md` — a system prompt for analysing off-plan purchase risks under wafi rules
- Write `prompts/investor-market-entry.md` — a bilingual system prompt for foreign investor onboarding scenarios
- Add Arabic tenant and landlord Q&A examples (`examples/tenant-question.ar.md`, `examples/landlord-question.ar.md`)
- Add English investor Q&A example (`examples/investor-question.en.md`) covering freehold zones and REGA requirements

---

## Phase 4 — MCP Integration

**Status:** ✅ مكتملة  
**Timeline:** Q4 2026

Expose the knowledge base as structured, callable tools through the Model Context Protocol so it can be used natively by Claude, GPT, and other MCP-compatible runtimes.

- Design and implement a Model Context Protocol (MCP) server that exposes datasets as typed tools
- Support tool calls for: `get_platform_info`, `get_authority_info`, `get_contract_type`, `lookup_term`
- Add Claude plugin manifest and OpenAI plugin manifest (`/.well-known/`) for API-based access
- Implement a lightweight structured query API (`scripts/query-dataset.py`) with filter, search, and export options
- Write integration documentation for connecting the MCP server to Claude Code and Claude Desktop
- Publish a Docker image for self-hosted MCP server deployment

---

## Phase 5 — Arabic Embeddings

**Status:** ⚪ Planned  
**Timeline:** Q1 2027

Produce an embedding-ready, chunked version of the knowledge base optimised for semantic search over Arabic and bilingual real estate content.

- Chunk all datasets and source documentation into embedding-ready segments with metadata headers
- Generate and publish a pre-built Arabic vector index using a public Arabic-capable embedding model
- Support semantic search over regulations, platform rules, contract clauses, and terminology
- Provide a `scripts/embed-and-index.py` script for local index regeneration
- Document integration patterns with LangChain, LlamaIndex, and pgvector
- Benchmark retrieval quality against a set of 20 canonical Saudi real estate questions

---

## Phase 6 — Community and Ecosystem

**Status:** ⚪ Planned  
**Timeline:** Q2 2027

Grow the project into a community-maintained ecosystem with standardised contribution tooling and integrations across major AI frameworks.

- Publish detailed contributor guidelines covering dataset standards, citation requirements, and review process
- Add pull request templates for new datasets, schema changes, and prompt additions
- Launch community dataset expansion for municipal zones, REGA fee schedules, and regional market data
- Publish a LangChain integration example using the MCP server and vector index together
- Publish a LlamaIndex integration example with a Saudi real estate Q&A agent
- Establish a versioning and changelog policy for dataset releases
