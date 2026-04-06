# Stats Practice Lab

A focused practice website built from a compiled statistics question bank.

## Features

- `55` questions in a clean practice flow
- random mode, sequential mode, and quick jump by question number
- per-user login
- synced progress tracking with `mastered` and `review later`
- immediate feedback for interactive choices plus worked-answer reveals
- saved answer history and recent activity
- Cloudflare Pages deployment with a D1-backed `_worker.js` API

## Local preview

1. Generate the question data and deployable files:

   ```bash
   python3 scripts/build_questions_data.py
   python3 scripts/prepare_dist.py
   ```

2. Serve the folder:

   ```bash
   python3 -m http.server 8788
   ```

3. Open `http://localhost:8788`.

## Deploy

This repo deploys to Cloudflare Pages in advanced mode using `_worker.js`.

Required Cloudflare setup:

- D1 database bound as `DB`
- Pages secret `AUTH_USERS_JSON`

Example secret shape:

```json
{
  "Howard": {
    "displayName": "Howard",
    "password": "Howieluvu"
  },
  "Freya": {
    "displayName": "Freya",
    "password": "1234567"
  }
}
```

Pages / Wrangler settings:

- Framework preset: `None`
- Build command: `python3 scripts/build_questions_data.py && python3 scripts/prepare_dist.py`
- Build output directory: `dist`

If you prefer Wrangler:

```bash
npx wrangler@latest pages deploy dist --project-name stats-practice-lab
```

To apply the schema:

```bash
npx wrangler@latest d1 migrations apply stats-practice-lab-db --remote
```
