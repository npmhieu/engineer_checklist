# Markdown to HTML

Requires Node.js 20 or newer. Install dependencies from the repository root:

```sh
npm ci --prefix tool
```

Convert a Markdown file:

```sh
node tool/md-to-html.mjs codex/basic/1.api_application/1.http_fundamentals.md
```

Creates `codex/basic/1.api_application/1.http_fundamentals.html` next to the source.
An existing HTML output with the same name is overwritten.
Paths resolve from the current working directory; quote paths containing spaces.

The output is a complete HTML document with embedded styles, tables, lists, links,
and fenced code blocks. Relative links and image paths stay unchanged. Inline HTML
is preserved, so use trusted Markdown files. Rendering uses [Marked](https://marked.js.org/).

```sh
node tool/md-to-html.mjs --help
```
