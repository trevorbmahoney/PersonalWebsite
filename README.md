# Trevor Mahoney — Portfolio

Personal site for Trevor Mahoney, senior product designer based in San Francisco. A single editorial page: hero, about, selected work, experience, contact.

Built with vanilla HTML, CSS, and JavaScript. No build step, no framework, no dependencies.

## Run locally

Any static file server works. From this directory:

```sh
python3 -m http.server 5173
```

Then open <http://localhost:5173>.

## Structure

- `index.html` — the entire site: markup, styles, and behavior in one file
- `assets/` — portrait and project case study images
- `.claude/` — local preview tooling

## Editing content

Project case studies and the resume timeline are inline data at the bottom of `index.html` (`window.PROJECTS` and `window.TIMELINE`). Edit there and reload — no rebuild required.
