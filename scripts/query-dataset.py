#!/usr/bin/env python3
"""Query Saudi real estate datasets from the terminal. Supports Arabic and English keywords."""

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

DATASETS = {
    "platforms":    REPO_ROOT / "data" / "platforms.ar.json",
    "authorities":  REPO_ROOT / "data" / "authorities.ar.json",
    "contracts":    REPO_ROOT / "data" / "contract-types.ar.json",
    "terms":        REPO_ROOT / "data" / "real-estate-terms.ar.json",
    "concepts":     REPO_ROOT / "data" / "market-concepts.ar.json",
}

NAME_FIELDS = {
    "platforms":   ("id", "name_ar", "name_en"),
    "authorities": ("id", "name_ar", "name_en"),
    "contracts":   ("id", "name_ar", "name_en"),
    "terms":       ("id", "term_ar", "term_en"),
    "concepts":    ("id", "concept_ar", "concept_en"),
}

GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def load_dataset(name: str) -> list[dict]:
    path = DATASETS[name]
    if not path.exists():
        print(f"Error: dataset file not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def matches_search(entry: dict, query: str) -> bool:
    """Case-insensitive substring search across all string values."""
    query_lower = query.lower()
    for value in entry.values():
        if isinstance(value, str) and query_lower in value.lower():
            return True
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and query_lower in item.lower():
                    return True
    return False


def matches_field(entry: dict, field_filter: str) -> bool:
    """Filter by field=value pair."""
    if "=" not in field_filter:
        print(f"Error: --field must be in format 'field=value', got: {field_filter}", file=sys.stderr)
        sys.exit(1)
    field, value = field_filter.split("=", 1)
    entry_val = entry.get(field.strip())
    if entry_val is None:
        return False
    return value.strip().lower() in str(entry_val).lower()


def print_table(entries: list[dict], dataset: str) -> None:
    id_field, ar_field, en_field = NAME_FIELDS[dataset]
    col_id  = max(len(id_field), max((len(e.get(id_field, "")) for e in entries), default=0))
    col_ar  = max(len(ar_field), max((len(e.get(ar_field, "")) for e in entries), default=0))
    col_ar  = min(col_ar, 40)
    col_en  = max(len(en_field), max((len(e.get(en_field, "")) for e in entries), default=0))
    col_en  = min(col_en, 50)

    header = (
        f"{BOLD}{id_field:<{col_id}}  {ar_field:<{col_ar}}  {en_field:<{col_en}}{RESET}"
    )
    print(header)
    print("-" * (col_id + col_ar + col_en + 4))
    for e in entries:
        row_id = e.get(id_field, "")[:col_id]
        row_ar = e.get(ar_field, "")[:col_ar]
        row_en = e.get(en_field, "")[:col_en]
        print(f"{CYAN}{row_id:<{col_id}}{RESET}  {YELLOW}{row_ar:<{col_ar}}{RESET}  {row_en:<{col_en}}")


def print_pretty(entries: list[dict]) -> None:
    for i, entry in enumerate(entries):
        if i > 0:
            print()
        print(f"{BOLD}{'─' * 60}{RESET}")
        for key, value in entry.items():
            if isinstance(value, list):
                print(f"  {GREEN}{key}{RESET}: {', '.join(str(v) for v in value)}")
            elif isinstance(value, dict):
                print(f"  {GREEN}{key}{RESET}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {GREEN}{key}{RESET}: {value}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query Saudi real estate datasets. Supports Arabic and English keywords.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python scripts/query-dataset.py -d platforms -l
  python scripts/query-dataset.py -d contracts -s "إيجار"
  python scripts/query-dataset.py -d authorities -f "type=هيئة تنظيمية"
  python scripts/query-dataset.py -d terms -s "ضريبة" -o pretty
  python scripts/query-dataset.py -d concepts -s "رؤية 2030" -o json
        """,
    )
    parser.add_argument(
        "-d", "--dataset",
        required=True,
        choices=list(DATASETS.keys()),
        metavar="DATASET",
        help=f"Dataset to query. Choices: {', '.join(DATASETS.keys())}",
    )
    parser.add_argument("-s", "--search",  metavar="KEYWORD", help="Search keyword (Arabic or English)")
    parser.add_argument("-f", "--field",   metavar="FIELD=VALUE", help="Filter by field, e.g. --field category=إيجار")
    parser.add_argument("-l", "--list",    action="store_true", help="List all entries (ID and name)")
    parser.add_argument(
        "-o", "--format",
        default="table",
        choices=["table", "json", "pretty"],
        help="Output format (default: table)",
    )
    args = parser.parse_args()

    entries = load_dataset(args.dataset)
    results = entries

    if args.search:
        results = [e for e in results if matches_search(e, args.search)]

    if args.field:
        results = [e for e in results if matches_field(e, args.field)]

    total = len(entries)
    found = len(results)
    print(f"\n{BOLD}Saudi Real Estate AI — {args.dataset.capitalize()} Dataset{RESET}")
    print(f"Total entries: {total} | Showing: {found}\n")

    if not results:
        print("No results found for query.")
        return

    if args.list or args.format == "table":
        print_table(results, args.dataset)
    elif args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.format == "pretty":
        print_pretty(results)


if __name__ == "__main__":
    main()
