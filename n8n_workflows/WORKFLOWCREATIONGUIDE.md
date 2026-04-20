# WORKFLOW CREATION GUIDE (Trend Pulse)

## Goal

Create n8n templates that stay consistent with the Trend Pulse architecture and monetization model.

## Naming convention

- Free: `free/NN_<keyword_or_usecase>_free.json`
- Premium: `premium/NN_<keyword_or_usecase>_pro.json`

## Mandatory node modules

1. **Intake**
2. **Enrichment**
3. **Scoring**
4. **Content generation**
5. **Publishing / exports**
6. **Logging**

## Error handling standard

- Add dedicated error branch/log payload.
- External API nodes must include retry behavior.

## Free vs premium differentiation

### Free
- fewer enrichment/scoring layers
- limited outputs
- lead magnet CTA

### Premium
- deeper enrichment
- stronger scoring (SEO + AEO + intent)
- multi-format outputs
- richer export destinations

## Template scaffold checklist

- [ ] workflow name follows convention
- [ ] module sequence matches Trend Pulse chain
- [ ] env placeholders instead of hardcoded secrets
- [ ] retries configured on external API nodes
- [ ] explicit error route and log record
- [ ] sample input payload in first Set node
- [ ] output contract documented in final payload node

## Completed premium templates

1. `04_ai_voice_generator_pro.json`
2. `05_local_llm_assistant_pro.json`
3. `06_private_gpt_rag_pro.json`
4. `07_ai_video_generator_pro.json`
5. `08_faceless_youtube_automation_pro.json`
6. `09_tiktok_ai_generator_pro.json`
7. `10_aeo_optimizer_pro.json`
8. `11_agentic_workflow_builder_pro.json`
9. `12_multimodal_pipeline_pro.json`

## V2 documentation alignment

When adding or renaming workflows:

1. Update `docs/v2/workflow-library-v2.md` and `docs/v2/link-map-v2.md`.
2. Add any new env keys to `docs/v2/env-vars-matrix.md`.
3. Record the change in `CHANGELOG.md` and `docs/v2/changelog-v2.md`.
4. If the workflow ships as an independent package under `workflows/<slug>/`, ensure `.env.example` matches the matrix row.
