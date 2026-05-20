#!/usr/bin/env python3
"""
validate-data.py — Validate Saudi Real Estate AI datasets against JSON schemas.

Usage:
    python scripts/validate-data.py
    python scripts/validate-data.py --verbose
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError, SchemaError
except ImportError:
    print("Error: jsonschema library is not installed. Run: pip install jsonschema")
    sys.exit(1)

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Detect repo root: the parent of the directory containing this script
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

# Mapping: dataset file (relative to repo root) → schema file (relative to repo root)
DATASETS = [
    ("data/platforms.ar.json", "schemas/platforms.schema.json"),
    ("data/platforms.en.json", "schemas/platforms.schema.json"),
    ("data/authorities.ar.json", "schemas/authorities.schema.json"),
    ("data/contract-types.ar.json", "schemas/contract-types.schema.json"),
]


def load_json(path: Path) -> object:
    """Load and return parsed JSON from a file."""
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_dataset(
    data_rel: str,
    schema_rel: str,
    verbose: bool,
) -> tuple[bool, str]:
    """
    Validate a single dataset against its schema.

    Returns (success: bool, message: str).
    """
    data_path = REPO_ROOT / data_rel
    schema_path = REPO_ROOT / schema_rel

    # Load schema
    try:
        schema = load_json(schema_path)
    except FileNotFoundError:
        return False, f"Schema file not found: {schema_rel}"
    except json.JSONDecodeError as exc:
        return False, f"Invalid JSON in schema {schema_rel}: {exc}"

    # Load dataset
    try:
        data = load_json(data_path)
    except FileNotFoundError:
        return False, f"Dataset file not found: {data_rel}"
    except json.JSONDecodeError as exc:
        return False, f"Invalid JSON in dataset {data_rel}: {exc}"

    # Determine entry count for display
    entry_count = len(data) if isinstance(data, list) else 1

    # Run validation
    try:
        validate(instance=data, schema=schema)
    except ValidationError as exc:
        detail = exc.message
        if verbose:
            detail = exc.message
            if exc.absolute_path:
                detail += f"\n     Path: {' -> '.join(str(p) for p in exc.absolute_path)}"
            if exc.context:
                sub_errors = "\n     ".join(e.message for e in exc.context[:3])
                detail += f"\n     Sub-errors: {sub_errors}"
        return False, detail
    except SchemaError as exc:
        return False, f"Schema is invalid: {exc.message}"

    return True, f"[{entry_count} entries]"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Saudi Real Estate AI datasets against JSON schemas."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print full ValidationError details on failure",
    )
    args = parser.parse_args()

    title = "Saudi Real Estate AI — Dataset Validation"
    separator = "=" * len(title)

    print(f"\n{BOLD}{title}{RESET}")
    print(separator)

    passed = 0
    failed = 0

    for data_rel, schema_rel in DATASETS:
        success, message = validate_dataset(data_rel, schema_rel, args.verbose)
        label = data_rel.ljust(40)
        if success:
            print(f"{GREEN}✓{RESET} {label} {message}")
            passed += 1
        else:
            print(f"{RED}✗{RESET} {label} {RED}FAILED:{RESET} {message}")
            failed += 1

    total = passed + failed
    print(separator)

    if failed == 0:
        summary_color = GREEN
    else:
        summary_color = RED if failed == total else YELLOW

    print(f"{summary_color}{BOLD}{passed}/{total} datasets valid{RESET}\n")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
