# n8n_workflows

Trend Pulse-aligned workflow library for:
1) high-growth SEO/AEO keyword targeting, and
2) workflow monetization through free + premium templates.

## V2 documentation (operator truth layer)

**Start here:** [`docs/v2/00-start-here.md`](./docs/v2/00-start-here.md)

**Workspace layout (real files in git, dual-repo policy, rsync):** [`docs/SESSION_EXPORT_REAL_TREES_AND_POLICY.md`](./docs/SESSION_EXPORT_REAL_TREES_AND_POLICY.md)

V2 adds a markdown “truth” layer beside the JSON templates:

- import + credentials discipline
- env var matrix across all templates
- Trend Pulse contract (stages + QA gates)
- full workflow inventory + keyword link map
- [`CHANGELOG.md`](./CHANGELOG.md) for library-level releases

**AutoTagger cross-links:** product/playbook narrative lives in `v5-workspace/playbooks/v2` and `v3`; AutoTag execution truth in `v5-workspace/docs/v2/`.

**V3 (Annex note) for this library:** [`docs/v3/00-annex.md`](./docs/v3/00-annex.md) — how n8n docs relate to creative Annex playbooks (no duplicate JSON).

**Canonical home:** this path is the full-weight library. See [`CANONICAL_HOME.md`](./CANONICAL_HOME.md). **Cursor:** [`.cursorignore`](./.cursorignore) trims indexing noise; **Git (optional):** [`.gitignore`](./.gitignore) is ready if you `git init` here.

## Repository structure

```
n8n_workflows/
├── docs/
│   ├── v2/                     # V2 operator docs (markdown)
│   └── v3/                     # Annex positioning note (markdown)
├── CHANGELOG.md                # Library changelog
├── workflows/                  # Independent self-contained packages
│   ├── WORKFLOWS_INDEX.md
│   ├── trend-analyzer-free/
│   ├── trend-analyzer-pro/
│   ├── ai-note-taker-pro/
│   ├── content-repurposing-pro/
│   ├── ai-voice-generator-pro/
│   ├── local-llm-assistant-pro/
│   ├── private-gpt-rag-pro/
│   ├── ai-video-generator-pro/
│   ├── faceless-youtube-automation-pro/
│   ├── tiktok-ai-generator-pro/
│   ├── aeo-optimizer-pro/
│   ├── agentic-workflow-builder-pro/
│   └── multimodal-pipeline-pro/
├── README.md
├── CHANGELOG.md
├── TRENDINGKEYWORDS2026.md
├── WORKFLOWCREATIONGUIDE.md
├── SUMMARY.md
├── COMPLETE_SUMMARY.md
├── free/
│   └── 01_trend_analyzer_free.json
└── premium/
    ├── 01_trend_analyzer_pro.json
    ├── 02_ai_note_taker_pro.json
    ├── 03_content_repurposing_pro.json
    ├── 04_ai_voice_generator_pro.json
    ├── 05_local_llm_assistant_pro.json
    ├── 06_private_gpt_rag_pro.json
    ├── 07_ai_video_generator_pro.json
    ├── 08_faceless_youtube_automation_pro.json
    ├── 09_tiktok_ai_generator_pro.json
    ├── 10_aeo_optimizer_pro.json
    ├── 11_agentic_workflow_builder_pro.json
    └── 12_multimodal_pipeline_pro.json
```

## Independent mode

Use `workflows/` when you want each template to be standalone.
Each package includes:
- `workflow.json`
- `README.md`
- `.env.example`

## Included templates

### Free (lead generation)
- **Trend Analyzer Free**

### Premium (commercial)
- **01-12 Pro workflow library** for trend intelligence, note-taking, repurposing, voice, local LLM, private GPT, video, faceless YouTube, TikTok, AEO, agentic automation, and multimodal orchestration.

## Trend Pulse node pattern

`intake -> enrichment -> scoring -> content generation -> publish/export -> logging`

## Environment variable placeholders

Common placeholders used in templates:
- `{{$env.OPENAI_API_KEY}}`
- `{{$env.WHISPERX_API_KEY}}`
- `{{$env.NOTION_TOKEN}}`
- `{{$env.SLACK_WEBHOOK_URL}}`
- `{{$env.APIFY_TOKEN}}`
- `{{$env.RUNWAY_API_KEY}}`
- `{{$env.YOUTUBE_API_TOKEN}}`
- `{{$env.ELEVENLABS_API_KEY}}`

## Import steps

1. Open n8n -> **Workflows** -> **Import from file**.
2. Import a JSON template from `free/` or `premium/` or from an independent package folder.
3. Open Credentials and map env-backed credentials.
4. Test with sample payload.
5. Activate workflow and optionally add schedule trigger.

## Monetization model

- **Free**: low-friction value + usage cap + CTA to premium.
- **Premium**: higher automation depth, richer AEO scoring, production outputs.
- Suggested packaging:
  - template bundle (one-time),
  - managed automation subscription (monthly),
  - done-for-you implementation upsell.
