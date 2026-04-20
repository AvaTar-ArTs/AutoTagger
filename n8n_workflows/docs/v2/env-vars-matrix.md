# Environment variables matrix (V2)

| Variable | Workflows (typical) | Notes |
|----------|---------------------|--------|
| `OPENAI_API_KEY` | 01–12 premium, free trend | Required for OpenAI nodes |
| `SLACK_WEBHOOK_URL` | 02, 03, 04, 07, 09, 11, 12 | Incoming webhook; do not log full URL |
| `WHISPERX_API_KEY` | 02 | Only if you keep the placeholder transcription URL |
| `NOTION_TOKEN` | 06, 12 | Notion API version header required in node |
| `APIFY_TOKEN` | (reserved / future) | Listed in README for Apify-backed runs |
| `ELEVENLABS_API_KEY` | 04 | Voice provider placeholder |
| `RUNWAY_API_KEY` | 07 | Video provider placeholder |
| `YOUTUBE_API_TOKEN` | 08 | OAuth bearer for YouTube Data API |
| `OLLAMA_BASE_URL` | 05 | Optional; default shown as `http://localhost:11434` in templates |

**Rule:** each `workflows/<slug>/.env.example` is the minimum set for that package.
