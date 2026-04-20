# n8n Trend Pulse library — start here (V2)

This is the **V2 operator index** for the workflow pack. The same tree ships inside **AutoTagger** at `n8n_workflows/` (full real directories in git) and may exist as an **optional second checkout** at `~/n8n_workflows` (`AvaTar-ArTs/n8n_workflows`); keep copies aligned with git or rsync, not symlinks — see [SESSION_EXPORT_REAL_TREES_AND_POLICY.md](../SESSION_EXPORT_REAL_TREES_AND_POLICY.md). Use this V2 index when:

- importing JSON into n8n,
- wiring credentials and env vars,
- selling bundles without over-claiming what each HTTP node does.

## Read order

| Doc | Purpose |
|-----|---------|
| [import-and-credentials.md](./import-and-credentials.md) | Import paths, credential mapping, first run |
| [env-vars-matrix.md](./env-vars-matrix.md) | One table of env keys → workflows |
| [trend-pulse-pattern.md](./trend-pulse-pattern.md) | Required node chain and QA |
| [workflow-library-v2.md](./workflow-library-v2.md) | Full inventory `01`–`12` + free + packages |
| [link-map-v2.md](./link-map-v2.md) | Keyword research row → workflow file |

## Related (AutoTagger repo)

- Product / operator narrative: `v5-workspace/playbooks/v2/` and `v5-workspace/playbooks/v3/`
- AutoTag runbooks: `v5-workspace/docs/v2/`
