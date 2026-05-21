# Saudi Real Estate AI — MCP Server

This MCP server exposes the `saudi-real-estate-ai` knowledge base as 8 structured tools that Claude Desktop and other MCP-compatible runtimes can call directly.

---

## Tools

| Tool | Dataset | Description |
|---|---|---|
| `search_terms` | `real-estate-terms.ar.json` | Search bilingual glossary (83 terms) |
| `get_property_type` | `property-types.ar.json` | Property definitions, deed types, ownership rules |
| `check_broker_requirements` | `broker-requirements.ar.json` | REGA broker licensing and ethics |
| `get_housing_programs` | `housing-programs.ar.json` | Sakani, REDF, NHC, ROSHN, and more |
| `get_reits_framework` | `reits-framework.ar.json` | CMA REIT rules and Tadawul requirements |
| `get_building_code` | `saudi-building-code.ar.json` | Saudi Building Code (SBC) requirements |
| `get_foreign_investor_rules` | `foreign-investor.ar.json` | Foreign ownership rules by nationality |
| `get_property_coding` | `property-coding.ar.json` | National Address, REDS, land parcel systems |

---

## Installation

```bash
git clone https://github.com/Samix2026/saudi-real-estate-ai.git
cd saudi-real-estate-ai
pip install mcp>=1.0.0
```

---

## Claude Desktop Configuration

Add the server to your Claude Desktop configuration file.

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

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

Replace `/absolute/path/to/saudi-real-estate-ai` with the absolute path to your local clone.

After saving, quit and relaunch Claude Desktop. The 8 tools will appear in the tool selector.

---

## Example Calls

```python
# Search for a term
search_terms(query="إيجار")

# Get all property types
get_property_type()

# Get a specific SBC code
get_building_code(code_id="sbc_201")

# Get REITs framework concepts about foreign investment
get_reits_framework(topic="foreign")

# Get foreign investor rules for GCC nationals
get_foreign_investor_rules(nationality="GCC")
```

---

## Disclaimer

> This server exposes informational data only. It does not constitute legal or financial advice. Always verify through official Saudi authorities (REGA, ejar, wafi, sakani) and consult licensed professionals before making any legal or financial decisions.
