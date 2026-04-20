#!/usr/bin/env python3
"""Generate Trend Pulse product HTML under playbooks/products/ and scenarios markdown."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRODUCTS_DIR = REPO / "v5-workspace" / "playbooks" / "products"
SCENARIOS_MD = REPO / "n8n_workflows" / "docs" / "v2" / "product-scenarios.md"

# slug, display name, tier, premium_json (None for free), tagline, inputs_hint, outputs_hint, example_title, example_body, personas
PRODUCTS: list[dict[str, str | None]] = [
    {
        "slug": "trend-analyzer-free",
        "name": "Trend Analyzer Free",
        "tier": "Free",
        "premium_json": "free/01_trend_analyzer_free.json",
        "tagline": "Lead-gen snapshot: one keyword row with SEO/AEO framing and a clean upgrade path.",
        "inputs": "keyword, variant_1, variant_2, intent",
        "outputs": "Single-keyword analysis plus CTA-friendly summary for landing pages.",
        "example_title": "Friday newsletter block",
        "example_body": "You plug in four variants of the same head term, compare intent labels, and export the strongest line for your hero + one bullet for social.",
        "personas": "Creators validating a hook before writing; agencies sampling the library.",
    },
    {
        "slug": "trend-analyzer-pro",
        "name": "Trend Analyzer Pro",
        "tier": "Premium",
        "premium_json": "premium/01_trend_analyzer_pro.json",
        "tagline": "Expand a seed topic into a scored keyword set for SEO/AEO and growth bets.",
        "inputs": "seed_topic, region",
        "outputs": "Expanded keyword set with scoring columns you can sort and feed into content ops.",
        "example_title": "New vertical in two cities",
        "example_body": "Seed with a product category + two metro regions; use the expanded set to brief writers and paid search teams the same Monday.",
        "personas": "Growth leads, SEO managers, product marketing.",
    },
    {
        "slug": "ai-note-taker-pro",
        "name": "AI Note Taker Pro",
        "tier": "Premium",
        "premium_json": "premium/02_ai_note_taker_pro.json",
        "tagline": "Turn recordings into structured notes, actions, owners, and a publish-ready payload.",
        "inputs": "audio_url, workspace_id",
        "outputs": "Structured notes with actions and owners for Notion/Slack handoff.",
        "example_title": "Sales call to CRM tasks",
        "example_body": "Drop a call URL after the demo; reviewers get bullet decisions and named follow-ups without re-listening.",
        "personas": "RevOps, founders, CS pods.",
    },
    {
        "slug": "content-repurposing-pro",
        "name": "Content Repurposing Pro",
        "tier": "Premium",
        "premium_json": "premium/03_content_repurposing_pro.json",
        "tagline": "Long-form in → channel-native variants out (threads, carousels, email blocks).",
        "inputs": "source_url or pasted long copy, tone presets",
        "outputs": "Channel packs with hooks and CTA variants sized for paid and organic.",
        "example_title": "Webinar replay week",
        "example_body": "One transcript becomes a LinkedIn carousel outline, three X threads, and a nurture email block with consistent claims.",
        "personas": "Content leads, demand gen, solo experts.",
    },
    {
        "slug": "ai-voice-generator-pro",
        "name": "AI Voice Generator Pro",
        "tier": "Premium",
        "premium_json": "premium/04_ai_voice_generator_pro.json",
        "tagline": "Script to voice pipeline for ads, explainers, and faceless narration.",
        "inputs": "script text, voice profile, pacing",
        "outputs": "Render-ready audio segments with filenames matched to storyboards.",
        "example_title": "30s product explainer",
        "example_body": "Paste a tight VO script; export stems for your editor and A/B two openings for paid social.",
        "personas": "Performance marketers, YouTube operators.",
    },
    {
        "slug": "local-llm-assistant-pro",
        "name": "Local LLM Assistant Pro",
        "tier": "Premium",
        "premium_json": "premium/05_local_llm_assistant_pro.json",
        "tagline": "Private assistant loop on hardware you control—no cloud transcript retention.",
        "inputs": "Model endpoint, system prompt, user message batch",
        "outputs": "Structured replies with citations to local context chunks when configured.",
        "example_title": "Policy Q&A inside the VPN",
        "example_body": "Point at an internal handbook index; teams ask operational questions without sending text to a public API.",
        "personas": "Security-conscious SMBs, regulated shops.",
    },
    {
        "slug": "private-gpt-rag-pro",
        "name": "Private GPT RAG Pro",
        "tier": "Premium",
        "premium_json": "premium/06_private_gpt_rag_pro.json",
        "tagline": "RAG over your corpus with retrieval gates and answer formatting for support.",
        "inputs": "doc collection id, user question, access scope",
        "outputs": "Answer + retrieved passage IDs for audit trails.",
        "example_title": "Tier-2 support deflection",
        "example_body": "Agents paste a ticket; workflow returns a draft reply with doc links they can paste into Zendesk.",
        "personas": "Support leads, IT knowledge teams.",
    },
    {
        "slug": "ai-video-generator-pro",
        "name": "AI Video Generator Pro",
        "tier": "Premium",
        "premium_json": "premium/07_ai_video_generator_pro.json",
        "tagline": "Storyboard → shot list → generative video hooks for short-form tests.",
        "inputs": "brief, aspect ratio, style references",
        "outputs": "Scene list + generation prompts + export checklist.",
        "example_title": "Three hooks for one offer",
        "example_body": "Ship Monday tests: same CTA, three visual metaphors, filenames that map to ad set IDs.",
        "personas": "Growth creatives, UGC coordinators.",
    },
    {
        "slug": "faceless-youtube-automation-pro",
        "name": "Faceless YouTube Automation Pro",
        "tier": "Premium",
        "premium_json": "premium/08_faceless_youtube_automation_pro.json",
        "tagline": "Title packs, descriptions, and chapter beats for faceless channels at volume.",
        "inputs": "niche, competitor URLs, posting cadence",
        "outputs": "Weekly slate of titles, hooks, and description templates.",
        "example_title": "Evergreen explainer channel",
        "example_body": "Feed two competitor channels; get a month of differentiated angles with compliance-friendly disclaimers.",
        "personas": "Faceless channel operators, editors.",
    },
    {
        "slug": "tiktok-ai-generator-pro",
        "name": "TikTok AI Generator Pro",
        "tier": "Premium",
        "premium_json": "premium/09_tiktok_ai_generator_pro.json",
        "tagline": "Native-feeling TikTok scripts and on-screen text beats from one brief.",
        "inputs": "product angle, sound trend id, duration cap",
        "outputs": "Hook + body + CTA lines with safe-claims language.",
        "example_title": "Drop-week micro-tests",
        "example_body": "Generate five 18s variants with different first-frame promises; pick two for spark ads.",
        "personas": "Social leads, creator managers.",
    },
    {
        "slug": "aeo-optimizer-pro",
        "name": "AEO Optimizer Pro",
        "tier": "Premium",
        "premium_json": "premium/10_aeo_optimizer_pro.json",
        "tagline": "Answer-engine readiness: entities, FAQs, and snippet targets from your page copy.",
        "inputs": "page URL or HTML, target queries",
        "outputs": "AEO patch list: headings, FAQ schema notes, internal link hints.",
        "example_title": "Pillar refresh before launch",
        "example_body": "Paste a long guide; get prioritized answer blocks for Chat-style surfaces without rewriting everything blind.",
        "personas": "SEO/AEO specialists, editorial leads.",
    },
    {
        "slug": "agentic-workflow-builder-pro",
        "name": "Agentic Workflow Builder Pro",
        "tier": "Premium",
        "premium_json": "premium/11_agentic_workflow_builder_pro.json",
        "tagline": "Compose multi-step agent graphs with guardrails and handoff nodes.",
        "inputs": "goal spec, tool allowlist, success checks",
        "outputs": "Draft n8n subgraph structure + human approval gates.",
        "example_title": "Research → brief → draft",
        "example_body": "Chain retrieval, summarizer, and editor bot with explicit stop points for human sign-off.",
        "personas": "Automation engineers, technical PMs.",
    },
    {
        "slug": "multimodal-pipeline-pro",
        "name": "Multimodal Pipeline Pro",
        "tier": "Premium",
        "premium_json": "premium/12_multimodal_pipeline_pro.json",
        "tagline": "Image + text + metadata intake into a single scored asset record.",
        "inputs": "mixed asset URLs, taxonomy tags",
        "outputs": "Unified records for DAM or PIM handoff.",
        "example_title": "Catalog ingestion Friday",
        "example_body": "Batch product shots and blurbs; emit CSV rows your merchandising tool can import.",
        "personas": "Ecom ops, data enrichment teams.",
    },
]


def _css() -> str:
    return """  <style>
    :root { --bg:#0c0f12; --line:#2a3340; --text:#e8edf2; --muted:#8b98a8; --mint:#5eead4; --sun:#fbbf24; --card:#121820; --accent2:#fb7185; }
    body { margin:0; font-family:"Syne",sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color: var(--mint); text-underline-offset: 3px; }
    a:focus-visible { outline: 2px solid var(--sun); outline-offset: 3px; }
    header { padding:2rem 1.25rem 1rem; max-width:900px; margin:0 auto; }
    nav { max-width:900px; margin:0 auto; padding:0 1.25rem 1rem; font-family:"JetBrains Mono",monospace; font-size:0.72rem; color:var(--muted); }
    main { max-width:900px; margin:0 auto; padding:0 1.25rem 3rem; }
    .tier { font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--sun); margin:0 0 0.35rem; }
    h1 { margin:0 0 0.5rem; font-size:1.65rem; }
    .lead { color:var(--muted); margin:0 0 1.5rem; max-width:62ch; }
    section { margin-bottom:1.75rem; border:1px solid var(--line); border-radius:14px; padding:1.1rem 1.2rem; background:var(--card); }
    section h2 { margin:0 0 0.5rem; font-size:0.95rem; color:var(--mint); }
    ul { margin:0.25rem 0 0; padding-left:1.1rem; color:var(--muted); font-size:0.9rem; }
    .links { font-family:"JetBrains Mono",monospace; font-size:0.78rem; word-break:break-all; }
    .links a { display:block; margin:0.35rem 0; }
    .example { background:#0a1018; border-radius:10px; padding:0.85rem 1rem; margin-top:0.5rem; color:var(--text); font-size:0.9rem; }
    footer { max-width:900px; margin:0 auto; padding:0 1.25rem 2rem; font-size:0.78rem; color:var(--muted); font-family:"JetBrains Mono",monospace; }
  </style>"""


def _product_page(p: dict[str, str | None]) -> str:
    slug = str(p["slug"])
    name = str(p["name"])
    tier = str(p["tier"])
    pj = str(p["premium_json"]) if p["premium_json"] else ""
    rel_pkg = f"../../../n8n_workflows/workflows/{slug}/"
    rel_json_root = f"../../../n8n_workflows/{pj}" if pj else rel_pkg + "workflow.json"
    scenario_link = f"../../../n8n_workflows/docs/v2/product-scenarios.md#{slug}"
    title = f"{name} — Trend Pulse"
    personas = str(p["personas"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@500;600&display=swap" rel="stylesheet">
{_css()}
</head>
<body>
  <header>
    <p class="tier">{tier}</p>
    <h1>{name}</h1>
    <p class="lead">{p["tagline"]}</p>
  </header>
  <nav aria-label="Breadcrumb"><a href="index.html">Products</a> · <a href="../v2/index.html">V2 hub</a> · <a href="../index.html">Playbooks</a></nav>
  <main>
    <section>
      <h2>Who it is for</h2>
      <p class="lead" style="margin:0;">{personas}</p>
    </section>
    <section>
      <h2>IO contract (from package README)</h2>
      <p class="lead" style="margin:0;"><strong>Inputs:</strong> {p["inputs"]}</p>
      <p class="lead" style="margin:0.5rem 0 0;"><strong>Outputs:</strong> {p["outputs"]}</p>
    </section>
    <section>
      <h2>Worked example</h2>
      <p class="lead" style="margin:0;"><strong>{p["example_title"]}</strong></p>
      <div class="example">{p["example_body"]}</div>
      <p class="lead" style="margin:0.75rem 0 0;font-size:0.85rem;">Longer narrative + sample rows: <a href="{scenario_link}">product-scenarios.md#{slug}</a></p>
    </section>
    <section>
      <h2>Technical artifacts</h2>
      <div class="links">
        <a href="{rel_pkg}README.md">Package README (markdown)</a>
        <a href="{rel_pkg}workflow.json">workflow.json</a>
        <a href="{rel_json_root}">Bundled JSON ({pj})</a>
      </div>
      <p class="lead" style="margin:0.75rem 0 0;font-size:0.82rem;">Credentials: wire keys in n8n per README / <a href="../../docs/v2/import-and-credentials.md">import-and-credentials.md</a> (add <code>.env</code> or n8n credentials from your providers).</p>
    </section>
    <section>
      <h2>Operator truth</h2>
      <div class="links">
        <a href="../../docs/v2/workflow-library-v2.md">workflow-library-v2.md</a>
        <a href="../../docs/v2/import-and-credentials.md">import-and-credentials.md</a>
        <a href="../../docs/v2/env-vars-matrix.md">env-vars-matrix.md</a>
      </div>
    </section>
  </main>
  <footer>Trend Pulse library · AutoTagger <code>n8n_workflows/</code></footer>
</body>
</html>
"""


def _index_html() -> str:
    cards = []
    for p in PRODUCTS:
        slug = p["slug"]
        tier = p["tier"]
        cards.append(
            f"""    <article>
      <p class="id">{tier}</p>
      <h2><a href="{slug}.html">{p["name"]}</a></h2>
      <p>{p["tagline"]}</p>
    </article>"""
        )
    cards_block = "\n".join(cards)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Trend Pulse — Product pages</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@500;600&display=swap" rel="stylesheet">
  <style>
    :root {{ --bg:#0c0f12; --line:#2a3340; --text:#e8edf2; --muted:#8b98a8; --mint:#5eead4; --sun:#fbbf24; --card:#121820; }}
    body {{ margin:0; font-family:"Syne",sans-serif; background:var(--bg); color:var(--text); line-height:1.45; }}
    a {{ color: var(--mint); }}
    a:focus-visible {{ outline: 2px solid var(--sun); outline-offset: 3px; }}
    header {{ padding:2rem 1.25rem 1rem; max-width:960px; margin:0 auto; }}
    nav {{ max-width:960px; margin:0 auto; padding:0 1.25rem 1rem; font-family:"JetBrains Mono",monospace; font-size:0.75rem; color:var(--muted); }}
    main {{ max-width:960px; margin:0 auto; padding:0 1.25rem 3rem; display:grid; gap:1rem; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); }}
    article {{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:1rem 1.1rem; transition: border-color .15s ease, transform .15s ease; }}
    article:hover {{ border-color:#3d4d62; transform: translateY(-2px); }}
    article h2 {{ margin:0 0 0.35rem; font-size:1rem; }}
    article h2 a {{ color: var(--text); text-decoration: none; }}
    article h2 a:hover {{ text-decoration: underline; text-decoration-color: var(--mint); }}
    .id {{ font-family:"JetBrains Mono",monospace; font-size:0.7rem; color:var(--sun); letter-spacing:0.06em; margin:0 0 0.35rem; }}
    p {{ margin:0; color:var(--muted); font-size:0.88rem; }}
    footer {{ max-width:960px; margin:0 auto; padding:0 1.25rem 2rem; font-size:0.8rem; color:var(--muted); font-family:"JetBrains Mono",monospace; }}
  </style>
</head>
<body>
  <header>
    <h1 style="margin:0 0 0.35rem;">Trend Pulse product pages</h1>
    <p style="margin:0;color:var(--muted);max-width:62ch;">Sales-ready one-pagers plus deep links into the self-contained n8n packages and V2 operator docs. Open locally or via any static server.</p>
  </header>
  <nav aria-label="Breadcrumb"><a href="../v2/index.html">V2 hub</a> / <a href="../index.html">Playbooks</a> / Products</nav>
  <main>
{cards_block}
  </main>
  <footer>Scenarios: <a href="../../../n8n_workflows/docs/v2/product-scenarios.md">n8n_workflows/docs/v2/product-scenarios.md</a> · Revenue deck: <a href="../../autotag_revenue_playbook.html">autotag_revenue_playbook.html</a></footer>
</body>
</html>
"""


def _scenarios_md() -> str:
    lines = [
        "# Trend Pulse — product scenarios (examples)",
        "",
        "Short narratives and sample inputs for each workflow. Pair with "
        "[`workflow-library-v2.md`](./workflow-library-v2.md) and package READMEs under "
        "`n8n_workflows/workflows/*/README.md`.",
        "",
    ]
    for p in PRODUCTS:
        slug = p["slug"]
        lines.extend(
            [
                f"## {slug}",
                "",
                f"**{p['name']}** ({p['tier']})",
                "",
                "### Scenario",
                "",
                str(p["example_body"]),
                "",
                "### Sample inputs (illustrative)",
                "",
                f"- {p['inputs']}",
                "",
                "### Expected shape of outputs",
                "",
                f"- {p['outputs']}",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    PRODUCTS_DIR.mkdir(parents=True, exist_ok=True)
    (PRODUCTS_DIR / "index.html").write_text(_index_html(), encoding="utf-8")
    for p in PRODUCTS:
        slug = str(p["slug"])
        (PRODUCTS_DIR / f"{slug}.html").write_text(_product_page(p), encoding="utf-8")
    SCENARIOS_MD.parent.mkdir(parents=True, exist_ok=True)
    SCENARIOS_MD.write_text(_scenarios_md(), encoding="utf-8")
    print(f"Wrote {len(PRODUCTS) + 1} HTML files under {PRODUCTS_DIR}")
    print(f"Wrote {SCENARIOS_MD}")


if __name__ == "__main__":
    main()
