# Clippy website

Static download page for [Clippy](https://github.com/AnujWadi-Git/Clippy). No build step.

- `clippy/index.html` is the page. `clippy/Clippy.dmg` is the download.
- Every push to `main` runs `scripts/check.py` and deploys to Cloudflare Pages.
- Pull requests run the checks only.

## One-time setup
Repo secrets: `CLOUDFLARE_API_TOKEN` (Pages: Edit), `CLOUDFLARE_ACCOUNT_ID`.
Optional repo variable `CF_PAGES_PROJECT` (defaults to `clippy`).

## Shipping a new app version
Copy the new `Clippy.dmg` from the app repo's Release into `clippy/`, commit, push.

Preview locally: `python3 -m http.server 8768` then open `/clippy/`.
