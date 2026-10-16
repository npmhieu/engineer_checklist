# Backend Learning Notes — Gemini

Lessons structured according to the [Backend / Software Developer Knowledge Checklist](../checklist.md).

For each topic, five foundational engineering questions are answered:
1. **What is it?**
2. **Why do we need it?**
3. **How to apply / implement / use it?**
4. **When should I NOT use this? (Trade-offs and anti-patterns)**
5. **How do I know I understand it?**

---

## 1. Basic / Fundamental

### API & Application

| Item | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| 1 | [HTTP Fundamentals](basic/api_application/1.http_fundamentals.md) | Protocols, request/response anatomy, methods, status codes, headers, and statelessness | Done |
| 2 | [API / Request-Response](basic/api_application/2.api_request_response.md) | Interface contracts, request-response cycle, backend processing pipelines, and error shapes | Done |
| 3 | [REST API](basic/api_application/3.rest_api.md) | Architectural constraints, resource modeling, URI conventions, CRUD semantics, and PUT vs. PATCH | Done |
| 4 | [CRUD Resource](basic/api_application/4.crud_resource.md) | Lifecycle operations, public vs storage models, hard vs soft deletes, and concurrency control | Done |
| 5 | [Request Validation](basic/api_application/5.request_validation.md) | Boundary checks, schema validation, strict allowlists, and structured field errors | Done |
| 6 | [Business Validation](basic/api_application/6.business_validation.md) | Domain invariants, rich domain entities, state-dependent checks, and race condition prevention | Done |
| 7 | [Error Handling](basic/api_application/7.error_handling.md) | Operational vs programmer errors, RFC 9457 problem details, centralized boundaries, and request tracing | Done |
| 8 | [HTTP Status Codes](basic/api_application/8.http_status_codes.md) | Semantic status classes (2xx, 3xx, 4xx, 5xx), headers, caching interactions, and decision matrices | Done |
| 9 | `Search / Filter / Sort` | *(Upcoming)* | Pending |
| 10 | `Pagination` | *(Upcoming)* | Pending |
| 11 | `API Versioning` | *(Upcoming)* | Pending |
| 12 | `Idempotency Basics` | *(Upcoming)* | Pending |
