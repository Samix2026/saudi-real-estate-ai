import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "data"


def _load(filename: str) -> Any:
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)


def search_terms(query: str) -> list[dict]:
    """Search the bilingual real estate glossary by keyword (Arabic or English)."""
    terms = _load("real-estate-terms.ar.json")
    q = query.lower()
    return [
        t for t in terms
        if q in t.get("name_ar", "").lower()
        or q in t.get("name_en", "").lower()
        or q in t.get("definition_ar", "").lower()
        or q in t.get("definition_en", "").lower()
    ]


def get_property_type(type_id: str = "") -> list[dict]:
    """Get property type definitions, deed types, and ownership restrictions.
    Pass type_id for a specific type or omit for all 15 types."""
    types = _load("property-types.ar.json")
    if not type_id:
        return types
    return [t for t in types if t.get("id") == type_id]


def check_broker_requirements(topic: str = "") -> dict:
    """Return REGA broker licensing requirements. Pass topic to filter
    (e.g. 'licensing', 'ethics', 'cpd') or omit for the full dataset."""
    data = _load("broker-requirements.ar.json")
    if not topic:
        return data
    topic_lower = topic.lower()
    if "entries" in data:
        filtered = [
            e for e in data["entries"]
            if topic_lower in json.dumps(e, ensure_ascii=False).lower()
        ]
        return {**data, "entries": filtered}
    return data


def get_housing_programs(audience: str = "") -> list[dict]:
    """Return national housing programs (Sakani, REDF, NHC, ROSHN, etc.).
    Pass audience to filter by beneficiary type or omit for all 7 programs."""
    programs = _load("housing-programs.ar.json")
    if not audience:
        return programs
    audience_lower = audience.lower()
    return [
        p for p in programs
        if audience_lower in json.dumps(p.get("beneficiaries_ar", []), ensure_ascii=False).lower()
        or audience_lower in json.dumps(p.get("audience", []), ensure_ascii=False).lower()
    ]


def get_reits_framework(topic: str = "") -> dict:
    """Return the Saudi REIT regulatory framework — CMA rules, investor rights,
    Tadawul listing requirements. Pass topic to filter or omit for full dataset."""
    data = _load("reits-framework.ar.json")
    if not topic:
        return data
    topic_lower = topic.lower()
    result = {k: v for k, v in data.items() if not isinstance(v, list)}
    for key in ("concepts", "investor_rights", "listing_requirements"):
        if key in data:
            filtered = [
                item for item in data[key]
                if topic_lower in json.dumps(item, ensure_ascii=False).lower()
            ]
            if filtered:
                result[key] = filtered
    return result


def get_building_code(code_id: str = "") -> dict:
    """Return Saudi Building Code (SBC) data — buyer rights and developer obligations.
    Pass code_id (e.g. 'sbc_201', 'sbc_801') or omit for the full framework."""
    data = _load("saudi-building-code.ar.json")
    if not code_id:
        return data
    codes = data.get("codes", [])
    matched = [c for c in codes if c.get("id") == code_id]
    return {**{k: v for k, v in data.items() if not isinstance(v, list)}, "codes": matched}


def get_foreign_investor_rules(nationality: str = "") -> dict:
    """Return foreign investor real estate ownership rules.
    Pass nationality category (e.g. 'GCC', 'iqama', 'non-resident') or omit for all rules."""
    data = _load("foreign-investor.ar.json")
    if not nationality:
        return data
    nationality_lower = nationality.lower()
    if nationality_lower in json.dumps(data, ensure_ascii=False).lower():
        return data
    return data


def get_property_coding(system_id: str = "") -> list[dict]:
    """Return Saudi property identification and coding systems.
    Pass system_id (e.g. 'national_address', 'deed_number') or omit for all 5 systems."""
    systems = _load("property-coding.ar.json")
    if not system_id:
        return systems
    return [s for s in systems if s.get("id") == system_id]
