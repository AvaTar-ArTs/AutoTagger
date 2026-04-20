# Session export — n8n_workflows real trees, dual repos, and policy

This document is a **detailed record** of work completed to make the Trend Pulse n8n library **fully material on disk inside AutoTagger** (no symbolic links to `~/n8n_workflows`), to align **documentation and ignore files**, and to keep an **optional second git repository** in sync at the policy level.

It is intended as a handoff for future you, collaborators, or agents: what changed, where it lives, how to verify it, and how to refresh either copy safely.

---

## 1. Goals (what “done” meant)

1. **No symlinks** under `AutoTagger/n8n_workflows/` for the heavy payload directories: `free/`, `premium/`, `workflows/`, `imports/` must be ordinary directories and files, identical in behavior to a normal clone.
2. **Git-tracked library** in AutoTagger so `git clone https://github.com/AvaTar-ArTs/AutoTagger` includes the workflow JSON and packages without any post-clone linking step.
3. **Single policy story** across:
   - `n8n_workflows/CANONICAL_HOME.md`
   - `n8n_workflows/WORKSPACE_POLICY.md`
   - `n8n_workflows/LOCAL_BASE_NOTE.md`
   - `n8n_workflows/CHANGELOG.md`
   - standalone repo `AvaTar-ArTs/n8n_workflows` (same filenames at repo root where applicable)
4. **Additive versioning** (do not delete history to “replace” content); **`.gitignore` may evolve** for hygiene without being treated as a policy violation (see `WORKSPACE_POLICY.md`).

---

## 2. Repositories and remotes

| Role | Path (local) | Remote | Default branch |
|------|----------------|--------|----------------|
| Main product repo | `/Users/steven/AutoTagger` | `https://github.com/AvaTar-ArTs/AutoTagger` | `main` |
| Optional workflow-only repo | `/Users/steven/n8n_workflows` | `https://github.com/AvaTar-ArTs/n8n_workflows` | `main` |

Library content in AutoTagger lives at:

`AutoTagger/n8n_workflows/`

---

## 3. Git commits (evidence)

These commits capture the bulk of the migration and follow-up doc alignment.

### AutoTagger (`AvaTar-ArTs/AutoTagger`)

| Commit | Summary |
|--------|---------|
| `4e99e65` | Track `n8n_workflows` JSON trees as real copies (no symlinks): remove ignore rules for `free/` / `premium/` / `workflows/` / `imports/`, sync content from canonical disk, update docs and `.cursorignore` commentary. |
| `177f1c4` | `CHANGELOG.md` note under V2 baseline corrected to describe **real directories in git**, not symlinks. |
| `ef84108` | Session export `docs/SESSION_EXPORT_REAL_TREES_AND_POLICY.md`, README / CHANGELOG / `00-start-here` links. |

### Earlier related context on the same branch (policy introduction and Cursor layout)

| Commit | Summary |
|--------|---------|
| `e9ef67d` | Add `n8n_workflows/WORKSPACE_POLICY.md` (version additively; `.gitignore` may change). |
| `8445f77` | Cursor indexing / canonical home pointer work. |

### Standalone `n8n_workflows` (`AvaTar-ArTs/n8n_workflows`)

| Commit | Summary |
|--------|---------|
| `d27abd7` | Align `CANONICAL_HOME.md`, `WORKSPACE_POLICY.md`, and `CHANGELOG.md` with AutoTagger: two real copies, alignment via git/rsync, not symlinks. |

---

## 4. Mechanical steps that were performed

### 4.1 Replace symlink directories with real copies (AutoTagger)

Symlinked `free`, `premium`, `workflows`, or `imports` (if present) were **removed** as directory entries, then content was copied from the canonical checkout with **rsync** so the AutoTagger tree is a **full mirror** of the directories on disk at `/Users/steven/n8n_workflows`:

```bash
# Example pattern (run from a shell; paths are absolute for clarity)
rsync -a --delete /Users/steven/n8n_workflows/free/       /Users/steven/AutoTagger/n8n_workflows/free/
rsync -a --delete /Users/steven/n8n_workflows/premium/    /Users/steven/AutoTagger/n8n_workflows/premium/
rsync -a --delete /Users/steven/n8n_workflows/workflows/ /Users/steven/AutoTagger/n8n_workflows/workflows/
rsync -a --delete /Users/steven/n8n_workflows/imports/   /Users/steven/AutoTagger/n8n_workflows/imports/
```

`rsync -a` preserves permissions and timestamps; `--delete` removes files in the destination that no longer exist in the source (use only when you intend a true mirror).

### 4.2 Verification (no symlinks)

```bash
for d in free premium workflows imports; do
  ls -ld "/Users/steven/AutoTagger/n8n_workflows/$d"
done
```

Expect **`drwx…`** lines. If you see **`lrwx…`**, that entry is still a symlink and should be replaced using the rsync flow above after removing the symlink.

```bash
file /Users/steven/AutoTagger/n8n_workflows/free
# Expect: directory (not "broken symbolic link" or "symbolic link")
```

---

## 5. Configuration files changed (AutoTagger root)

### 5.1 `.gitignore`

- **Removed** ignore rules that prevented `n8n_workflows/free`, `premium`, `workflows`, and `imports` from being committed.
- **Left** ignores for large or generated areas (for example `v6-workspace/`, `output/`, archives, venvs).
- **Comment** at the `n8n_workflows` section states that full real trees are tracked.

### 5.2 `.cursorignore` (Cursor indexing)

- **Does not** ignore the n8n JSON trees by default (so agents can index them when needed).
- **Optional** commented block at the bottom allows ignoring `n8n_workflows/premium/` and `n8n_workflows/workflows/` if the index becomes too large — wording states that trees are **real copies in git**, not symlinks to `~/n8n_workflows`.

---

## 6. Markdown files created or updated (library root)

| File | Purpose |
|------|---------|
| `WORKSPACE_POLICY.md` | Do not remove—version instead; two copies without symlinks; `.gitignore` may evolve. |
| `CANONICAL_HOME.md` | Describes **in-repo** full copy under AutoTagger and optional second checkout at `~/n8n_workflows`. |
| `LOCAL_BASE_NOTE.md` | AutoTagger-local note: all trees real; optional **rsync from** `~/n8n_workflows` **into** AutoTagger when refreshing. |
| `CHANGELOG.md` | Library history; notes updated so JSON layout is described as real dirs in git. |

This file (`docs/SESSION_EXPORT_REAL_TREES_AND_POLICY.md`) is the **long-form export** of the session decisions and commands.

---

## 7. Keeping the two copies aligned (no symlinks)

**Allowed:** merge, cherry-pick, manual copy, **`rsync` then `git add` / commit** in the repo where you want history to live.

**Not used for this layout:** symlinks from AutoTagger into `~/n8n_workflows` for `free/`, `premium/`, `workflows/`, or `imports/`.

### Refresh AutoTagger from `~/n8n_workflows`

Use the rsync block in section 4.1, then from AutoTagger:

```bash
cd /Users/steven/AutoTagger
git status
git add n8n_workflows/
git commit -m "sync: n8n_workflows from canonical checkout"
git push origin main
```

### Push changes from AutoTagger toward `~/n8n_workflows`

Reverse the rsync source and destination (same four directories), then commit inside `/Users/steven/n8n_workflows` if that repo should carry the change.

---

## 8. What gets cloned where

| Clone | You get |
|-------|--------|
| `git clone …/AutoTagger.git` | Full `n8n_workflows/` including JSON and `docs/v2`, `docs/v3` as tracked in that repo. |
| `git clone …/n8n_workflows.git` | Workflow library as a standalone project (same logical content; maintain parity via git or rsync as you prefer). |

---

## 9. Operator documentation (unchanged by this session, but part of “everything”)

V2 operator docs remain the day-to-day truth for **import, credentials, env vars, and inventory**:

- Start: `docs/v2/00-start-here.md`
- Import: `docs/v2/import-and-credentials.md`
- Env matrix: `docs/v2/env-vars-matrix.md`
- Pattern: `docs/v2/trend-pulse-pattern.md`
- Library: `docs/v2/workflow-library-v2.md`
- Link map: `docs/v2/link-map-v2.md`
- Annex note: `docs/v3/00-annex.md`

This session export is **about repository layout and policy**, not replacing those operator guides.

---

## 10. “Save everything” checklist

1. **AutoTagger:** `git status` clean; `git push origin main` done through at least `ef84108` (session export) and subsequent doc-only commits on `main` if present.
2. **Standalone:** `git push origin main` after `d27abd7` for policy alignment.
3. After any local rsync, **commit** in the repo that should own the change so history stays reproducible.

---

## 11. Document history

| Date | Change |
|------|--------|
| 2026-04-20 | Initial session export authored and linked from `README.md` / `CHANGELOG.md`. |
