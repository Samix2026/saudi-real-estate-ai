# Phase 2 Knowledge Base Expansion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 new datasets, 5 schemas, 20+ terms, and README updates to complete the Saudi real estate AI knowledge base with property types, building code, REITs, housing programs, and property coding systems.

**Architecture:** Each task creates one data file + one schema file, registers both in validate-data.py, then validates. Terms file is updated last. README updates come at the end.

**Tech Stack:** JSON, JSON Schema draft-07, Python 3 (jsonschema), Markdown

---

## Task 1: Property Types Dataset + Schema

**Files:**
- Create: `data/property-types.ar.json`
- Create: `schemas/property-types.schema.json`
- Modify: `scripts/validate-data.py` (add to DATASETS list)

- [ ] **Step 1: Create the schema**

`schemas/property-types.schema.json` — validates an array of property type objects with required fields: id, name_ar, name_en, category, legal_definition_ar, legal_definition_en, deed_type_ar, permitted_uses_ar, restrictions_ar, typical_ownership_ar, foreign_ownership_allowed, registration_platform_ar, audience, source_url, last_verified.

- [ ] **Step 2: Create the data file with 15 entries**

`data/property-types.ar.json` — 15 entries covering all required types.

- [ ] **Step 3: Register in validate-data.py**

Add `("data/property-types.ar.json", "schemas/property-types.schema.json")` to DATASETS list.

- [ ] **Step 4: Run validation**

`python3 scripts/validate-data.py`
Expected: 8/8 datasets valid

---

## Task 2: Saudi Building Code Dataset + Schema

**Files:**
- Create: `data/saudi-building-code.ar.json`
- Create: `schemas/saudi-building-code.schema.json`
- Modify: `scripts/validate-data.py`

- [ ] **Step 1: Create schema** supporting the nested structure (versions array, codes array, buyer_rights array, developer_obligations array)

- [ ] **Step 2: Create data file** with 2 versions, 8 SBC codes, 6 buyer rights, 6 developer obligations

- [ ] **Step 3: Register in validate-data.py**

- [ ] **Step 4: Run validation** — 9/9 valid

---

## Task 3: REITs Framework Dataset + Schema

**Files:**
- Create: `data/reits-framework.ar.json`
- Create: `schemas/reits-framework.schema.json`
- Modify: `scripts/validate-data.py`

- [ ] **Step 1: Create schema** for object with regulatory_authorities, concepts, investor_rights, listing_requirements

- [ ] **Step 2: Create data file** with 10 concepts + 5 listing requirements

- [ ] **Step 3: Register + validate** — 10/10 valid

---

## Task 4: Housing Programs Dataset + Schema

**Files:**
- Create: `data/housing-programs.ar.json`
- Create: `schemas/housing-programs.schema.json`
- Modify: `scripts/validate-data.py`

- [ ] **Step 1: Create schema** for array of housing program entries

- [ ] **Step 2: Create data file** with 7 programs

- [ ] **Step 3: Register + validate** — 11/11 valid

---

## Task 5: Property Coding Dataset + Schema

**Files:**
- Create: `data/property-coding.ar.json`
- Create: `schemas/property-coding.schema.json`
- Modify: `scripts/validate-data.py`

- [ ] **Step 1: Create schema** for array of coding system entries

- [ ] **Step 2: Create data file** with 5 coding systems

- [ ] **Step 3: Register + validate** — 12/12 valid

---

## Task 6: Update real-estate-terms.ar.json

**Files:**
- Modify: `data/real-estate-terms.ar.json` (add 20 terms, existing 64 → 84+)

Note: The schema has a category enum: عقود, تراخيص, منصات, تمويل, ملكية, إجراءات, جهات تنظيمية. New terms must use one of these existing categories or the schema must be updated first.

- [ ] **Step 1: Add 20 new terms** across SBC, REITs, housing programs, and coding categories

- [ ] **Step 2: Validate** — all 12 datasets valid

---

## Task 7: Update README.md and README.ar.md

**Files:**
- Modify: `README.md` (Scope table)
- Modify: `README.ar.md` (Scope table)

- [ ] **Step 1: Add 5 rows to the Scope table in README.md**
- [ ] **Step 2: Add matching 5 rows to README.ar.md**
- [ ] **Step 3: Final validation** — 12/12 datasets valid
