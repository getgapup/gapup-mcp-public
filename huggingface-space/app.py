"""Gapup MCP — HF Spaces live browser.

Fetches the live tool list from https://mcp.gapup.io/mcp and renders a
searchable explorer with install snippets. No API key required to browse —
the tools/list endpoint is anonymous-friendly. Tool calls require a free
GAPUP_API_KEY (get one at https://hub.gapup.io/agents-api/onboard).
"""
from __future__ import annotations

import json
import os
from datetime import datetime

import gradio as gr
import requests

MCP_ENDPOINT = "https://mcp.gapup.io/mcp"
HEALTH_ENDPOINT = "https://mcp.gapup.io/health"
ONBOARD_URL = "https://hub.gapup.io/agents-api/onboard"
PUBLIC_REPO = "https://github.com/getgapup/gapup-mcp-public"


def fetch_tools() -> tuple[list[dict], str]:
    """Call tools/list and return (tools, status_message)."""
    try:
        resp = requests.post(
            MCP_ENDPOINT,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
            },
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}),
            timeout=20,
        )
        resp.raise_for_status()
        # SSE-style — find the first data: line
        for line in resp.text.splitlines():
            if line.startswith("data:"):
                payload = json.loads(line[5:].strip())
                tools = payload.get("result", {}).get("tools", [])
                return tools, f"✓ Live · {len(tools)} tools · refreshed {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
        return [], "✗ No data line in response"
    except Exception as e:
        return [], f"✗ Fetch error : {e}"


def fetch_health() -> dict:
    try:
        return requests.get(HEALTH_ENDPOINT, timeout=10).json()
    except Exception:
        return {}


def filter_tools(tools: list[dict], query: str) -> list[list[str]]:
    """Return rows for the gr.Dataframe — name, description, link."""
    q = (query or "").lower().strip()
    rows = []
    for t in tools:
        name = t.get("name", "")
        desc = (t.get("description", "") or "")[:240]
        if q and q not in name.lower() and q not in desc.lower():
            continue
        rows.append([name, desc])
    return rows


INSTALL_SNIPPETS = {
    "Claude Desktop / Cursor / Windsurf (JSON)": """{
  "mcpServers": {
    "gapup": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.gapup.io/mcp",
               "--header", "Authorization: Bearer ${GAPUP_API_KEY}"],
      "env": { "GAPUP_API_KEY": "<paste your free key here>" }
    }
  }
}""",
    "Smithery one-click": "smithery mcp add gapup-team/gapup-mcp",
    "Raw curl (no SDK)": """curl -X POST https://mcp.gapup.io/mcp \\
  -H "Authorization: Bearer $GAPUP_API_KEY" \\
  -H "Content-Type: application/json" \\
  -H "Accept: application/json, text/event-stream" \\
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'""",
    "Python (mcp SDK)": """from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import os, asyncio

async def main():
    headers = {"Authorization": f"Bearer {os.environ['GAPUP_API_KEY']}"}
    async with streamablehttp_client("https://mcp.gapup.io/mcp", headers=headers) as (r, w, _):
        async with ClientSession(r, w) as s:
            await s.initialize()
            result = await s.list_tools()
            print(f"{len(result.tools)} tools available")

asyncio.run(main())""",
}


def render_snippet(name: str) -> str:
    return INSTALL_SNIPPETS.get(name, "")


# ─── UI ──────────────────────────────────────────────────────────────────────

with gr.Blocks(
    title="Gapup MCP — 185+ agent-payable C-suite tools",
    theme=gr.themes.Soft(primary_hue="amber", neutral_hue="slate"),
) as demo:
    gr.Markdown(
        f"""
        # 🏛️ Gapup MCP — 185+ agent-payable C-suite expertise tools

        Hosted MCP server at `{MCP_ENDPOINT}` · Pay-per-call **x402 USDC/EURC** ·
        **100 free calls/month** · [Get a free key]({ONBOARD_URL})

        Browse the live tool catalogue below. Each tool is callable from any
        MCP-compliant client (Claude, Cursor, Windsurf, VS Code, …).
        """
    )

    with gr.Row():
        with gr.Column(scale=3):
            search = gr.Textbox(
                label="Search tools",
                placeholder="e.g. competitor, sec, kyc, sanctions, clinical, esg, …",
                show_label=False,
            )
        with gr.Column(scale=1):
            refresh_btn = gr.Button("↻ Refresh", variant="secondary")

    status = gr.Markdown("Loading live catalogue…")
    table = gr.Dataframe(
        headers=["Tool name", "Description"],
        datatype=["str", "str"],
        col_count=(2, "fixed"),
        wrap=True,
        interactive=False,
        max_height=600,
    )

    # State
    cached_tools = gr.State([])

    def refresh():
        tools, msg = fetch_tools()
        return tools, msg, filter_tools(tools, "")

    def on_search(query, tools):
        return filter_tools(tools, query)

    demo.load(refresh, outputs=[cached_tools, status, table])
    refresh_btn.click(refresh, outputs=[cached_tools, status, table])
    search.change(on_search, inputs=[search, cached_tools], outputs=table)

    gr.Markdown("## Install in your MCP client")
    with gr.Row():
        snippet_choice = gr.Dropdown(
            choices=list(INSTALL_SNIPPETS.keys()),
            value="Claude Desktop / Cursor / Windsurf (JSON)",
            label="Pick a client",
        )
    snippet_code = gr.Code(
        value=INSTALL_SNIPPETS["Claude Desktop / Cursor / Windsurf (JSON)"],
        language="json",
        label="Config / snippet",
    )
    snippet_choice.change(render_snippet, inputs=snippet_choice, outputs=snippet_code)

    gr.Markdown(
        f"""
        ---
        ### Resources

        - **Free API key** (100 calls/mo, no card) → [{ONBOARD_URL}]({ONBOARD_URL})
        - **Examples** (curl / TS / Python) — [docs/EXAMPLES.md]({PUBLIC_REPO}/blob/main/docs/EXAMPLES.md)
        - **Quickstart 5 min** — [docs/QUICKSTART.md]({PUBLIC_REPO}/blob/main/docs/QUICKSTART.md)
        - **Pricing T0 → T5** — [docs/PRICING.md]({PUBLIC_REPO}/blob/main/docs/PRICING.md)
        - **60+ data sources** — [docs/CONNECTORS.md]({PUBLIC_REPO}/blob/main/docs/CONNECTORS.md)
        - **Public repo (MIT)** — [{PUBLIC_REPO}]({PUBLIC_REPO})

        Contact : `agents@gapup.io`
        """
    )


if __name__ == "__main__":
    demo.launch()
