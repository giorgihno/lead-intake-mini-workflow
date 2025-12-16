# Mini Lead Intake Demo Repo

WIP - see PRs for changes.

## Run locally
```bash
python scripts/validate_payload.py examples/sample-payload.json

```

## Branching strategy
- No direct commits to `main` (PRs only).
- Feature branches use `feature/*`.
- PRs are merged using **merge commits** to preserve history and merge points.

## How to review commit history
- Each PR contains focused commits.
- `main` shows merge commits corresponding to PRs (schema → validator → docs).
