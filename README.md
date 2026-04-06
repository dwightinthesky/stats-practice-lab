# Stats Practice Lab

A focused practice website built from a compiled statistics question bank.

## Features

- `55` questions in a clean practice flow
- random mode, sequential mode, and quick jump by question number
- local progress tracking with `mastered` and `review later`
- reveal-answer workflow for self-testing
- static site, so it deploys cleanly to Cloudflare Pages

## Local preview

1. Generate the question data:

   ```bash
   python3 scripts/build_questions_data.py
   ```

2. Serve the folder:

   ```bash
   python3 -m http.server 8788
   ```

3. Open `http://localhost:8788`.

## Deploy

This repo is static. On Cloudflare Pages:

- Framework preset: `None`
- Build command: leave empty
- Build output directory: `/`

If you prefer Wrangler:

```bash
npx wrangler@latest pages deploy . --project-name stats-practice-lab
```

