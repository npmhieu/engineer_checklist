# Backend learning notes — Codex

Lessons follow [the backend checklist](../checklist.md). The current review template asks:

1. What is it?
2. Why do we need it?
3. Under the hood: how does it work one layer deeper?
   - Tools/engines: data structures, runtime cost, memory and disk I/O.
   - Patterns/standards: lifecycle boundaries, state changes, client and infrastructure behavior.
4. How do we apply / implement / use it? Include happy and unhappy paths.
5. When should I NOT use this? What are the trade-offs and anti-patterns?
6. How do I know I understand it? Explain from a blank page and predict failures when constraints change.

Lessons 4–12 answer all six questions, with analogies, mechanism walkthroughs, runnable examples, and constraint-change exercises. Lessons 1–3 retain the original three-question format and review practice.

## Basic / Fundamental → API & Application

Read these lessons in order:

1. [HTTP Fundamentals](basic/api_application/1.http_fundamentals.md) — the communication protocol.
2. [API / Request-Response](basic/api_application/2.api_request_response.md) — the application contract and processing flow.
3. [REST API](basic/api_application/3.rest_api.md) — an architectural style and resource-oriented API design.
4. [CRUD Resource](basic/api_application/4.crud_resource.md) — managing resource lifecycles and choosing where CRUD fits.
5. [Request Validation](basic/api_application/5.request_validation.md) — checking incoming data against the API contract.
6. [Business Validation](basic/api_application/6.business_validation.md) — enforcing application invariants, including concurrent writes.
7. [Error Handling](basic/api_application/7.error_handling.md) — preserving state and reporting failures safely.
8. [HTTP Status Codes](basic/api_application/8.http_status_codes.md) — selecting response outcomes, headers, and content.
9. [Search / Filter / Sort](basic/api_application/9.search_filter_sort.md) — finding authorized records and returning deterministic results.
10. [Pagination](basic/api_application/10.pagination.md) — bounding responses and continuing through ordered data.
11. [API Versioning](basic/api_application/11.api_versioning.md) — evolving contracts while supported clients coexist.
12. [Idempotency Basics](basic/api_application/12.idempotency_basics.md) — handling repeated intent without duplicate committed effects.

Filename numbers match the item order in this checklist subsection, continuing the existing `1.`–`3.` naming convention.

Each lesson includes examples and review practice. Lessons 4–7 and 9–12 contain independent Python 3 standard-library examples; save each Python block as the filename shown and run it with `python3 filename.py`. They exercise individual layers, not a complete API. Lesson 8 supplies a small local HTTP server and curl commands for real responses. No package installation is needed.

The broader task API remains an illustrative contract, not a complete supplied application. Pseudocode is framework-neutral; curl examples in lessons 1–3 require your own local implementation. The lesson 8 server implements only its documented subset.

Checklist boxes track your learning progress. Mark an item complete when you can answer its review questions and work through its practice scenarios.
