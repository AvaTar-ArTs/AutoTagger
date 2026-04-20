# Import and credentials

## Import locations

1. **Curated bundles:** `premium/NN_*.json`, `free/01_*.json`
2. **Independent packages:** `workflows/<slug>/workflow.json` (each folder has its own `README.md` and `.env.example`)

n8n UI: **Workflows → Import from File**.

## Credentials pattern

Templates reference OpenAI and HTTP nodes using **environment variables** (e.g. `{{$env.OPENAI_API_KEY}}`). In n8n:

- Create credentials that read from env, **or**
- Replace with your vault-backed credentials and keep the same node graph.

Never commit real API keys into JSON.

## First run checklist

1. Import one workflow (recommend `premium/01_trend_analyzer_pro.json` as baseline).
2. Set env vars listed in [env-vars-matrix.md](./env-vars-matrix.md).
3. Run **Manual Trigger** with sample `Set` node inputs unchanged first.
4. Confirm each HTTP Request URL matches a provider you actually use; swap placeholders where noted in workflow meta.
