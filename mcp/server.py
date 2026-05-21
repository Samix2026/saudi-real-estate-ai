import asyncio
import json

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from . import tools

app = Server("saudi-real-estate-ai")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_terms",
            description="Search the Saudi real estate bilingual glossary (83 terms) by keyword in Arabic or English.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search keyword in Arabic or English"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_property_type",
            description="Get definitions, deed types, and ownership restrictions for Saudi property types (15 types).",
            inputSchema={
                "type": "object",
                "properties": {
                    "type_id": {
                        "type": "string",
                        "description": "Property type ID (e.g. 'villa', 'apartment') — omit for all types"
                    }
                }
            }
        ),
        Tool(
            name="check_broker_requirements",
            description="Get REGA real estate broker licensing requirements, CPD obligations, and ethics rules.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic filter (e.g. 'licensing', 'ethics', 'cpd') — omit for full dataset"
                    }
                }
            }
        ),
        Tool(
            name="get_housing_programs",
            description="Get Saudi national housing programs — Sakani, REDF, NHC, ROSHN, rental subsidy, and more.",
            inputSchema={
                "type": "object",
                "properties": {
                    "audience": {
                        "type": "string",
                        "description": "Audience filter (e.g. 'مواطن', 'citizen', 'first-time') — omit for all 7 programs"
                    }
                }
            }
        ),
        Tool(
            name="get_reits_framework",
            description="Get the Saudi REIT regulatory framework — CMA rules, investor rights, Tadawul listing requirements.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic filter (e.g. 'distribution', 'foreign', 'listing') — omit for full framework"
                    }
                }
            }
        ),
        Tool(
            name="get_building_code",
            description="Get Saudi Building Code (SBC) requirements, buyer rights, and developer obligations.",
            inputSchema={
                "type": "object",
                "properties": {
                    "code_id": {
                        "type": "string",
                        "description": "SBC code ID (e.g. 'sbc_201', 'sbc_801') — omit for full framework"
                    }
                }
            }
        ),
        Tool(
            name="get_foreign_investor_rules",
            description="Get foreign investor real estate ownership rules by nationality — GCC nationals, Iqama holders, non-residents.",
            inputSchema={
                "type": "object",
                "properties": {
                    "nationality": {
                        "type": "string",
                        "description": "Nationality category (e.g. 'GCC', 'iqama', 'non-resident') — omit for all rules"
                    }
                }
            }
        ),
        Tool(
            name="get_property_coding",
            description="Get Saudi property identification systems — National Address, REDS title registration, land parcel numbers.",
            inputSchema={
                "type": "object",
                "properties": {
                    "system_id": {
                        "type": "string",
                        "description": "Coding system ID (e.g. 'national_address', 'deed_number') — omit for all 5 systems"
                    }
                }
            }
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    tool_map = {
        "search_terms":             lambda a: tools.search_terms(a.get("query", "")),
        "get_property_type":        lambda a: tools.get_property_type(a.get("type_id", "")),
        "check_broker_requirements": lambda a: tools.check_broker_requirements(a.get("topic", "")),
        "get_housing_programs":     lambda a: tools.get_housing_programs(a.get("audience", "")),
        "get_reits_framework":      lambda a: tools.get_reits_framework(a.get("topic", "")),
        "get_building_code":        lambda a: tools.get_building_code(a.get("code_id", "")),
        "get_foreign_investor_rules": lambda a: tools.get_foreign_investor_rules(a.get("nationality", "")),
        "get_property_coding":      lambda a: tools.get_property_coding(a.get("system_id", "")),
    }
    if name not in tool_map:
        raise ValueError(f"Unknown tool: {name}")
    result = tool_map[name](arguments)
    return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
