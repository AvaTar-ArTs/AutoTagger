# AutoTagger n8n_workflows (this folder)

This path is the **AutoTagger-local** copy of the Trend Pulse n8n library:

- **All trees are real directories** in git: `free/`, `premium/`, `workflows/`, `imports/`, plus `docs/` and top-level markdown.
- There are **no symlinks** here. Clones get a complete, self-contained library.

## Optional sync with your other clone

If you also keep a checkout at `/Users/steven/n8n_workflows`, refresh this copy when needed:

```bash
rsync -a --delete /Users/steven/n8n_workflows/free/       /Users/steven/AutoTagger/n8n_workflows/free/
rsync -a --delete /Users/steven/n8n_workflows/premium/    /Users/steven/AutoTagger/n8n_workflows/premium/
rsync -a --delete /Users/steven/n8n_workflows/workflows/ /Users/steven/AutoTagger/n8n_workflows/workflows/
rsync -a --delete /Users/steven/n8n_workflows/imports/   /Users/steven/AutoTagger/n8n_workflows/imports/
```

Then commit any intentional changes in the AutoTagger repo.
