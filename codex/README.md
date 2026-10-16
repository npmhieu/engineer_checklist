# Backend learning notes — Codex

Lessons follow [the backend checklist](../checklist.md). The current review template asks:

1. What is it?
2. Why do we need it?
3. How do we apply / implement / use it?
4. When should I NOT use this? What are the trade-offs and anti-patterns?
5. How do I know I understand it?

Lessons 4–8 answer all five questions. Lessons 1–3 retain the original three-question format and review practice.

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

Filename numbers match the item order in this checklist subsection, continuing the existing `1.`–`3.` naming convention.

Each lesson includes examples and review practice. The task API is an illustrative contract, not a supplied server. Pseudocode is framework-neutral; curl commands require a local implementation listening on port 3000.

Checklist boxes track your learning progress. Mark an item complete when you can answer its review questions and work through its practice scenarios.
