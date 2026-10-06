# Clippy website

Static download page for [Clippy](https://github.com/AnujWadi-Git/Clippy). No build step.

- `clippy/index.html` is the page. `clippy/Clippy.dmg` is the download.
- Every push and pull request runs `scripts/check.py` (CI).
- Deploying is manual: upload this folder in Cloudflare Pages, or run the Deploy workflow by hand.

## One-time setup
Repo secrets: `CLOUDFLARE_API_TOKEN` (Pages: Edit), `CLOUDFLARE_ACCOUNT_ID`.
Optional repo variable `CF_PAGES_PROJECT` (defaults to `clippy-for-mac`).

## Shipping a new app version
Copy the new `Clippy.dmg` from the app repo's Release into `clippy/`, commit, push.

Preview locally: `python3 -m http.server 8768` then open `/clippy/`.
