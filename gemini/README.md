# Backend Learning Notes — Gemini

Lessons structured according to the [Backend / Software Developer Knowledge Checklist](../checklist.md).

For each topic, foundational engineering questions are answered:
1. **What is it?** (Plain sentence + real-world mental model)
2. **Why do we need it?** (Specific pains, bugs, or bottlenecks without it)
3. **Under the hood / The Mechanism / System Flow** (One layer deeper: data structures, lifecycle, runtime costs)
4. **How to apply / implement / use it?** (Minimal working example covering happy and unhappy paths)
5. **When should I NOT use this?** (Trade-offs, hidden costs, and anti-patterns)
6. **How do I know I understand it?** (Blank-page test and constraint change predictions)

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
| 9 | [Search / Filter / Sort](basic/api_application/9.search_filter_sort.md) | Query params, allowlists, dynamic WHERE/ORDER BY, indexing strategies, and full-text vs. B-Tree | Done |
| 10 | [Pagination](basic/api_application/10.pagination.md) | Offset vs. Cursor/Keyset vs. Time-based pagination, page drift, deep offset pitfalls, and Link headers | Done |
| 11 | [API Versioning](basic/api_application/11.api_versioning.md) | URI vs. Header vs. Query vs. Content Negotiation, breaking changes, adapter layers, and deprecation headers | Done |
| 12 | [Idempotency Basics](basic/api_application/12.idempotency_basics.md) | RFC 9110 method semantics, Idempotency-Key pattern, distributed locking, payload hashing, and retry safety | Done |

### Authentication & Authorization

| Item | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| 1 | [Authentication](basic/authentication_authorization/1.authentication.md) | Identity verification, perimeter pipelines, stateful vs stateless mechanisms, and context propagation | Done |
| 2 | [Authorization](basic/authentication_authorization/2.authorization.md) | Coarse vs. fine-grained access control, BOLA/IDOR prevention, policy decision tuples, and RBAC/ABAC/ReBAC | Done |
| 3 | [User Management](basic/authentication_authorization/3.user_management.md) | Identity lifecycle state machines, canonical normalization, token_version revocation, and GDPR anonymization | Done |
| 4 | [Role-Based Access Control (RBAC)](basic/authentication_authorization/4.role_based_access_control.md) | NIST 5-table schema, permission checking vs role checking, permission resolution, and avoiding role explosion | Done |
| 5 | `Session / Token` | *(Upcoming)* | Pending |
| 6 | `JWT Basics` | *(Upcoming)* | Pending |
| 7 | `Password / Credential Security` | *(Upcoming)* | Pending |
