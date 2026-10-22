#!/usr/bin/env node

import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { marked } from 'marked';

const usage = 'Usage: node tool/md-to-html.mjs <file.md>';
const args = process.argv.slice(2);

function escapeHtml(text) {
  return text.replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  })[character]);
}

async function main() {
  if (args.length === 1 && ['--help', '-h'].includes(args[0])) {
    console.log(usage);
    return;
  }
  if (args.length !== 1) {
    throw new Error(usage);
  }

  const inputPath = path.resolve(args[0]);
  const extension = path.extname(inputPath);
  if (extension.toLowerCase() !== '.md') {
    throw new Error('Input must be a .md file.');
  }

  const markdown = (await readFile(inputPath, 'utf8')).replace(/^\uFEFF/, '');
  const outputPath = inputPath.slice(0, -extension.length) + '.html';
  const title = escapeHtml(path.basename(inputPath, extension));
  const body = marked.parse(markdown, { gfm: true });
  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${title}</title>
  <style>
    body { max-width: 960px; margin: 40px auto; padding: 0 20px; color: #24292f; font: 16px/1.6 system-ui, sans-serif; overflow-wrap: break-word; }
    h1, h2, h3 { line-height: 1.25; margin-top: 1.5em; }
    a { color: #0969da; }
    pre, code { background: #f6f8fa; border-radius: 6px; }
    code { padding: 0.15em 0.3em; font-size: 0.9em; }
    pre { padding: 16px; overflow-x: auto; }
    pre code { padding: 0; }
    table { display: block; max-width: 100%; overflow-x: auto; border-collapse: collapse; }
    th, td { border: 1px solid #d0d7de; padding: 8px 12px; text-align: left; }
    th { background: #f6f8fa; }
    blockquote { margin-left: 0; padding-left: 16px; border-left: 4px solid #d0d7de; color: #57606a; }
    img { max-width: 100%; height: auto; }
  </style>
</head>
<body>
<main>
${body}</main>
</body>
</html>
`;

  await writeFile(outputPath, html, 'utf8');
  console.log(`Created ${outputPath}`);
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
});
