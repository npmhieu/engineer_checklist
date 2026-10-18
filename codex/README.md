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

Basic API & Application lessons 4–12, all current lessons in the other Basic / Fundamental subsections, and all current Intermediate, Advanced, and Testing & Acceptance lessons answer all six questions, with analogies, mechanism walkthroughs, runnable examples, and constraint-change exercises. Basic API & Application lessons 1–3 retain the original three-question format and review practice.

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

## Basic / Fundamental → Authentication & Authorization

1. [Authentication](basic/authentication_authorization/1.authentication.md) — verifying identity evidence and creating trusted caller context.
2. [Authorization](basic/authentication_authorization/2.authorization.md) — enforcing action, resource, ownership, and tenant boundaries.
3. [User Management](basic/authentication_authorization/3.user_management.md) — coordinating account lifecycle, proofs, suspension, and access state.
4. [Role-Based Access Control (RBAC)](basic/authentication_authorization/4.role_based_access_control.md) — grouping permissions into scoped roles with additional resource checks.
5. [Session / Token](basic/authentication_authorization/5.session_token.md) — maintaining authenticated continuity, expiry, rotation, and revocation.
6. [JWT Basics](basic/authentication_authorization/6.jwt_basics.md) — verifying structured claims against fixed cryptographic and application policy.
7. [Password / Credential Security](basic/authentication_authorization/7.password_credential_security.md) — protecting password verifiers, machine secrets, recovery, and credential lifecycle.

## Basic / Fundamental → Database

1. [Database Fundamentals](basic/database/1.database_fundamentals.md) — query execution, persistence, coordination, and recovery.
2. [Schema / Data Modeling](basic/database/2.schema_data_modeling.md) — entities, units, identity, and storage invariants.
3. [Relationships](basic/database/3.relationships.md) — cardinality, optionality, associations, and joins.
4. [Normalization](basic/database/4.normalization.md) — fact ownership, dependencies, and update anomalies.
5. [Primary / Foreign Key](basic/database/5.primary_foreign_key.md) — identity and reference integrity, including tenant scope.
6. [Indexes](basic/database/6.indexes.md) — access paths and their read/write trade-offs.
7. [Basic Query Optimization](basic/database/7.basic_query_optimization.md) — query count, plans, result semantics, and measured work.
8. [Transactions](basic/database/8.transactions.md) — local atomicity, concurrency boundaries, and uncertain outcomes.
9. [Migration Basics](basic/database/9.migration_basics.md) — tracked schema/data transitions and deployment compatibility.

## Basic / Fundamental → Common Features

1. [File Upload](basic/common_features/1.file_upload.md) — bounded intake, content policy, and safe publication.
2. [File Storage](basic/common_features/2.file_storage.md) — object identity, ownership, integrity, and recovery.
3. [Notifications](basic/common_features/3.notifications.md) — recoverable delivery intent and bounded retries.
4. [Export / Import](basic/common_features/4.export_import.md) — portable contracts, validation, and batch atomicity.
5. [Audit Log](basic/common_features/5.audit_log.md) — attributable evidence coordinated with committed changes.
6. [Reporting / Analytics](basic/common_features/6.reporting_analytics.md) — metric definitions, fact grain, and time-window correctness.

## Basic / Fundamental → Architecture & Code Organization

1. [Monolithic Architecture](basic/architecture_code_organization/1.monolithic_architecture.md) — deployment unity with internal module boundaries.
2. [Layered Architecture](basic/architecture_code_organization/2.layered_architecture.md) — transport, use-case, and persistence responsibilities.
3. [Separation of Concerns](basic/architecture_code_organization/3.separation_of_concerns.md) — cohesive policy and explicit effects.
4. [Package / Folder Organization](basic/architecture_code_organization/4.package_folder_organization.md) — import-safe modules and clear entry points.
5. [Dependency Direction](basic/architecture_code_organization/5.dependency_direction.md) — core ports, outer adapters, and composition.
6. [API / Worker / Cron Separation](basic/architecture_code_organization/6.api_worker_cron_separation.md) — shared rules behind distinct triggers and workloads.

## Basic / Fundamental → Testing

1. [Unit Test](basic/testing/1.unit_test.md) — isolated behavior, boundaries, and deterministic assertions.
2. [Integration Test](basic/testing/2.integration_test.md) — real component boundaries, fixtures, and persisted outcomes.

## Basic / Fundamental → Development & Operations

1. [Git](basic/development_operations/1.git.md) — snapshots, staging, history, and safe collaboration concepts.
2. [Environment / Configuration](basic/development_operations/2.environment_configuration.md) — typed startup settings and safe deployment boundaries.
3. [Logging](basic/development_operations/3.logging.md) — bounded, correlated, redacted operational events.
4. [Health Check](basic/development_operations/4.health_check.md) — distinct startup, readiness, and liveness actions.
5. [Basic Monitoring](basic/development_operations/5.basic_monitoring.md) — bounded signals, distributions, and actionable alerts.
6. [Basic CI/CD](basic/development_operations/6.basic_ci_cd.md) — required checks, artifact identity, and controlled promotion.

## Intermediate → API & Application

1. [Advanced API Design](intermediate/api_application/1.advanced_api_design.md) — concurrent edits, preconditions, bounded interfaces, and operation lifecycles.
2. [Backward Compatibility](intermediate/api_application/2.backward_compatibility.md) — preserving supported consumer behavior through mixed-version transitions.
3. [API Contract](intermediate/api_application/3.api_contract.md) — one described interface, schema checks, and executable provider expectations.
4. [Advanced Idempotency](intermediate/api_application/4.advanced_idempotency.md) — crash recovery, leases/fences, stable downstream identities, and uncertain effects.
5. [Rate Limiting](intermediate/api_application/5.rate_limiting.md) — atomic scoped admission, burst/refill behavior, and capacity trade-offs.
6. [Webhook](intermediate/api_application/6.webhook.md) — authenticated raw-body intake, durable inbox acceptance, and duplicate handling.
7. [Third-party API Integration](intermediate/api_application/7.third_party_api_integration.md) — bounded retries/deadlines, response validation, and provider failure mapping.
8. [Service-to-Service Communication](intermediate/api_application/8.service_to_service_communication.md) — workload identity, user delegation, resource scope, and propagated budgets.

## Intermediate → Database & Performance

1. [Advanced Transactions](intermediate/database_performance/1.advanced_transactions.md)
2. [Concurrency](intermediate/database_performance/2.concurrency.md)
3. [Race Conditions](intermediate/database_performance/3.race_conditions.md)
4. [Optimistic Locking](intermediate/database_performance/4.optimistic_locking.md)
5. [Pessimistic Locking](intermediate/database_performance/5.pessimistic_locking.md)
6. [Query Optimization](intermediate/database_performance/6.query_optimization.md)
7. [Database Migration in Production](intermediate/database_performance/7.database_migration_in_production.md)
8. [Caching](intermediate/database_performance/8.caching.md)
9. [Redis](intermediate/database_performance/9.redis.md)
10. [Connection Pooling](intermediate/database_performance/10.connection_pooling.md)

## Intermediate → Async / Background Processing

1. [Background Task](intermediate/async_background_processing/1.background_task.md)
2. [Job](intermediate/async_background_processing/2.job.md)
3. [Message](intermediate/async_background_processing/3.message.md)
4. [Producer](intermediate/async_background_processing/4.producer.md)
5. [Message Queue](intermediate/async_background_processing/5.message_queue.md)
6. [Consumer](intermediate/async_background_processing/6.consumer.md)
7. [Worker](intermediate/async_background_processing/7.worker.md)
8. [Cronjob](intermediate/async_background_processing/8.cronjob.md)
9. [Event](intermediate/async_background_processing/9.event.md)
10. [Event-Driven Architecture](intermediate/async_background_processing/10.event_driven_architecture.md)
11. [Queue vs Topic](intermediate/async_background_processing/11.queue_vs_topic.md)
12. [Job Status / Lifecycle](intermediate/async_background_processing/12.job_status_lifecycle.md)
13. [Retry](intermediate/async_background_processing/13.retry.md)
14. [Exponential Backoff](intermediate/async_background_processing/14.exponential_backoff.md)
15. [Timeout](intermediate/async_background_processing/15.timeout.md)
16. [Dead Letter Queue (DLQ)](intermediate/async_background_processing/16.dead_letter_queue.md)
17. [Duplicate Processing](intermediate/async_background_processing/17.duplicate_processing.md)
18. [Idempotent Consumer](intermediate/async_background_processing/18.idempotent_consumer.md)

## Intermediate → Application Features

1. [Async Export / Import](intermediate/application_features/1.async_export_import.md)
2. [Notification Architecture](intermediate/application_features/2.notification_architecture.md)
3. [Audit / Activity History](intermediate/application_features/3.audit_activity_history.md)
4. [Reporting Architecture](intermediate/application_features/4.reporting_architecture.md)
5. [Batch Processing](intermediate/application_features/5.batch_processing.md)

## Intermediate → Architecture

1. [Feature / Domain-oriented Architecture](intermediate/architecture/1.feature_domain_oriented_architecture.md)
2. [Modular Monolith](intermediate/architecture/2.modular_monolith.md)
3. [DDD Basics](intermediate/architecture/3.ddd_basics.md)
4. [Bounded Context](intermediate/architecture/4.bounded_context.md)
5. [Domain Service](intermediate/architecture/5.domain_service.md)
6. [Application Service](intermediate/architecture/6.application_service.md)
7. [Infrastructure Layer](intermediate/architecture/7.infrastructure_layer.md)
8. [Hybrid Architecture](intermediate/architecture/8.hybrid_architecture.md)
9. [Shared Platform / Infrastructure](intermediate/architecture/9.shared_platform_infrastructure.md)

## Intermediate → Testing

1. [End-to-End (E2E) Test](intermediate/testing/1.end_to_end_test.md)
2. [Contract Test](intermediate/testing/2.contract_test.md)
3. [Regression Test](intermediate/testing/3.regression_test.md)
4. [Smoke Test](intermediate/testing/4.smoke_test.md)
5. [Load Test](intermediate/testing/5.load_test.md)
6. [Basic Performance Test](intermediate/testing/6.basic_performance_test.md)

## Intermediate → Observability

1. [Structured Logging](intermediate/observability/1.structured_logging.md)
2. [Metrics](intermediate/observability/2.metrics.md)
3. [Error Tracking](intermediate/observability/3.error_tracking.md)
4. [Monitoring](intermediate/observability/4.monitoring.md)
5. [Alerting](intermediate/observability/5.alerting.md)
6. [Request ID](intermediate/observability/6.request_id.md)
7. [Correlation ID](intermediate/observability/7.correlation_id.md)
8. [Distributed Tracing](intermediate/observability/8.distributed_tracing.md)

## Intermediate → Deployment

1. [Docker / Containers](intermediate/deployment/1.docker_containers.md)
2. [CI/CD Pipeline](intermediate/deployment/2.ci_cd_pipeline.md)
3. [Production Deployment](intermediate/deployment/3.production_deployment.md)
4. [Database Migration Strategy](intermediate/deployment/4.database_migration_strategy.md)
5. [Rollback](intermediate/deployment/5.rollback.md)
6. [Feature Flags](intermediate/deployment/6.feature_flags.md)

## Advanced → Distributed Systems

1. [Distributed Systems Fundamentals](advanced/distributed_systems/1.distributed_systems_fundamentals.md)
2. [Service Boundaries](advanced/distributed_systems/2.service_boundaries.md)
3. [Microservices Architecture](advanced/distributed_systems/3.microservices_architecture.md)
4. [Inter-service Communication](advanced/distributed_systems/4.inter_service_communication.md)
5. [Event-Driven Architecture at Scale](advanced/distributed_systems/5.event_driven_architecture_at_scale.md)
6. [Event Schema / Versioning](advanced/distributed_systems/6.event_schema_versioning.md)
7. [Event Ordering](advanced/distributed_systems/7.event_ordering.md)
8. [Event Replay](advanced/distributed_systems/8.event_replay.md)
9. [Fan-out](advanced/distributed_systems/9.fan_out.md)
10. [Consumer Groups](advanced/distributed_systems/10.consumer_groups.md)

## Advanced → Messaging

1. [Message Delivery Semantics](advanced/messaging/1.message_delivery_semantics.md)
2. [At-most-once Delivery](advanced/messaging/2.at_most_once_delivery.md)
3. [At-least-once Delivery](advanced/messaging/3.at_least_once_delivery.md)
4. [Effectively-once Processing](advanced/messaging/4.effectively_once_processing.md)
5. [Exactly-once Concepts](advanced/messaging/5.exactly_once_concepts.md)
6. [Message Ordering](advanced/messaging/6.message_ordering.md)
7. [Poison Messages](advanced/messaging/7.poison_messages.md)
8. [Advanced Retry Strategies](advanced/messaging/8.advanced_retry_strategies.md)
9. [Dead Letter Queue Strategy](advanced/messaging/9.dead_letter_queue_strategy.md)
10. [Queue Backpressure](advanced/messaging/10.queue_backpressure.md)

## Advanced → Distributed Consistency

1. [Eventual Consistency](advanced/distributed_consistency/1.eventual_consistency.md)
2. [Strong Consistency](advanced/distributed_consistency/2.strong_consistency.md)
3. [CAP Theorem](advanced/distributed_consistency/3.cap_theorem.md)
4. [Distributed Transactions](advanced/distributed_consistency/4.distributed_transactions.md)
5. [Saga Pattern](advanced/distributed_consistency/5.saga_pattern.md)
6. [Compensation](advanced/distributed_consistency/6.compensation.md)
7. [Distributed Locking](advanced/distributed_consistency/7.distributed_locking.md)
8. [Distributed Idempotency](advanced/distributed_consistency/8.distributed_idempotency.md)

## Advanced → Database / Scaling

1. [Replication](advanced/database_scaling/1.replication.md)
2. [Read Replicas](advanced/database_scaling/2.read_replicas.md)
3. [Database Failover](advanced/database_scaling/3.database_failover.md)
4. [Partitioning](advanced/database_scaling/4.partitioning.md)
5. [Sharding](advanced/database_scaling/5.sharding.md)
6. [Consistency Models](advanced/database_scaling/6.consistency_models.md)
7. [Large-scale Data Architecture](advanced/database_scaling/7.large_scale_data_architecture.md)

## Advanced → Reliability

1. [Circuit Breaker](advanced/reliability/1.circuit_breaker.md)
2. [Bulkhead](advanced/reliability/2.bulkhead.md)
3. [Graceful Degradation](advanced/reliability/3.graceful_degradation.md)
4. [Fault Tolerance](advanced/reliability/4.fault_tolerance.md)
5. [High Availability](advanced/reliability/5.high_availability.md)
6. [Failover](advanced/reliability/6.failover.md)
7. [Disaster Recovery](advanced/reliability/7.disaster_recovery.md)
8. [Backup / Restore](advanced/reliability/8.backup_restore.md)
9. [Recovery Point Objective (RPO)](advanced/reliability/9.recovery_point_objective.md)
10. [Recovery Time Objective (RTO)](advanced/reliability/10.recovery_time_objective.md)
11. [Multi-Region Architecture](advanced/reliability/11.multi_region_architecture.md)

## Advanced → Performance

1. [Performance Engineering](advanced/performance/1.performance_engineering.md)
2. [Profiling](advanced/performance/2.profiling.md)
3. [Capacity Planning](advanced/performance/3.capacity_planning.md)
4. [Bottleneck Analysis](advanced/performance/4.bottleneck_analysis.md)
5. [Throughput Optimization](advanced/performance/5.throughput_optimization.md)
6. [Latency Optimization](advanced/performance/6.latency_optimization.md)
7. [Large-scale Caching](advanced/performance/7.large_scale_caching.md)

## Advanced → Observability / Operations

1. [Advanced Distributed Tracing](advanced/observability_operations/1.advanced_distributed_tracing.md)
2. [Service Level Objectives (SLO)](advanced/observability_operations/2.service_level_objectives.md)
3. [Service Level Agreements (SLA)](advanced/observability_operations/3.service_level_agreements.md)
4. [Error Budget](advanced/observability_operations/4.error_budget.md)
5. [Capacity Monitoring](advanced/observability_operations/5.capacity_monitoring.md)
6. [Advanced Alerting](advanced/observability_operations/6.advanced_alerting.md)
7. [Chaos Testing](advanced/observability_operations/7.chaos_testing.md)

## Advanced → Security

1. [Security Architecture](advanced/security/1.security_architecture.md)
2. [Threat Modeling](advanced/security/2.threat_modeling.md)
3. [Secrets Management](advanced/security/3.secrets_management.md)
4. [Encryption](advanced/security/4.encryption.md)
5. [Key Management](advanced/security/5.key_management.md)
6. [Advanced API Security](advanced/security/6.advanced_api_security.md)
7. [Zero Trust Concepts](advanced/security/7.zero_trust_concepts.md)
8. [Dependency / Supply-chain Security](advanced/security/8.dependency_supply_chain_security.md)

## Advanced → DevOps / Delivery

1. [Infrastructure as Code](advanced/devops_delivery/1.infrastructure_as_code.md)
2. [Blue-Green Deployment](advanced/devops_delivery/2.blue_green_deployment.md)
3. [Canary Deployment](advanced/devops_delivery/3.canary_deployment.md)
4. [Progressive Delivery](advanced/devops_delivery/4.progressive_delivery.md)
5. [Advanced Feature Flags](advanced/devops_delivery/5.advanced_feature_flags.md)
6. [Kubernetes](advanced/devops_delivery/6.kubernetes.md)
7. [Multi-environment Deployment](advanced/devops_delivery/7.multi_environment_deployment.md)

## Testing & Acceptance → Automated Testing

1. [Unit Test](testing_acceptance/automated_testing/1.unit_test.md)
2. [Integration Test](testing_acceptance/automated_testing/2.integration_test.md)
3. [Contract Test](testing_acceptance/automated_testing/3.contract_test.md)
4. [E2E Test](testing_acceptance/automated_testing/4.e2e_test.md)
5. [Regression Test](testing_acceptance/automated_testing/5.regression_test.md)
6. [Smoke Test](testing_acceptance/automated_testing/6.smoke_test.md)
7. [Load Test](testing_acceptance/automated_testing/7.load_test.md)
8. [Stress Test](testing_acceptance/automated_testing/8.stress_test.md)
9. [Performance Test](testing_acceptance/automated_testing/9.performance_test.md)
10. [Security Test](testing_acceptance/automated_testing/10.security_test.md)
11. [Chaos Test](testing_acceptance/automated_testing/11.chaos_test.md)

## Testing & Acceptance → Acceptance

1. [Acceptance Criteria](testing_acceptance/acceptance/1.acceptance_criteria.md)
2. [User Acceptance Testing (UAT)](testing_acceptance/acceptance/2.user_acceptance_testing.md)
3. [Factory Acceptance Testing (FAT)](testing_acceptance/acceptance/3.factory_acceptance_testing.md)

These Testing & Acceptance lessons consolidate scope, evidence, failure cases, and release/acceptance decisions. Test labels are not mutually exclusive: one E2E scenario can also be a regression, security, and automated acceptance test. UAT adds intended-user business judgment; FAT is a supplier-handover activity where the project agreement calls for it, not a mandatory stage for every backend release.

Filename numbers match item order within each checklist subsection and restart at `1.` in a new subsection. Use this numbered index or numeric filename sorting; plain lexicographic sorting can place `10.` before `2.`. Checklist boxes remain unchanged: publishing a lesson does not prove you have learned it.

## Running Examples

Each lesson includes examples and review practice. API & Application lessons 4–7 and 9–12, plus Authentication & Authorization lessons 1–5, contain independent Python 3 standard-library examples; save each Python block as the filename shown and run it with `python3 filename.py`. They exercise individual layers, not a complete API. API & Application lesson 8 supplies a small local HTTP server and curl commands for real responses.

Authentication & Authorization lesson 6 uses PyJWT; lesson 7 uses argon2-cffi. Each includes virtual-environment installation/run commands. These maintained libraries avoid teaching handwritten JWT verification or password hashing. Examples were checked with PyJWT 2.15.1 and argon2-cffi 25.1.0; project dependencies are unchanged.

All 29 lessons in Database, Common Features, Architecture & Code Organization, Testing, and Development & Operations include independent Python 3 standard-library examples. Save the Python block under its stated filename and run `python3 filename.py`; the two testing examples run `unittest` directly. The Git example additionally requires Git on PATH and uses a temporary repository without committing. File/package/pipeline examples write only disposable temporary fixtures; they do not deploy, send messages, or alter this repository. No additional package installation is needed for these 29 lessons.

SQLite examples demonstrate SQLite behavior, not production-database parity, concurrent-load performance, or crash/power-loss proof. Other examples isolate a specific boundary rather than supplying a complete production application. Each lesson states relevant omissions, expected happy/unhappy outcomes, and references.

Intermediate API & Application lessons use independent offline examples: seven require only Python 3's standard library; API Contract additionally uses jsonschema (checked with 4.26.0) and includes isolated virtual-environment commands. No project dependencies change. Network/provider effects and authenticated contexts are controlled fixtures, not production security or real third-party integrations. File-backed crash/reopen examples use temporary databases; retry/deadline examples use fake clocks rather than real sleeps.

The 62 Intermediate lessons from Database & Performance through Deployment each include one independent offline Python standard-library example. All 62 examples were checked with Python 3.12.0 and SQLite 3.42.0. Save and run the block using the filename shown. SQLite examples use real local transactions and disposable databases; other examples may model broker, worker, platform, or deployment boundaries rather than run those products. Each page labels these limits. Database Migration Strategy additionally requires SQLite 3.35+ for its DROP COLUMN demonstration. Examples do not deploy, contact providers, send notifications, or install dependencies.

Redis includes optional commands for your own private Redis instance; Docker / Containers includes an optional real Dockerfile and build/run walkthrough requiring Docker Engine and a base-image pull. Those optional service commands are separate from the offline checks. PostgreSQL, Redis, RabbitMQ, Kubernetes, hosted CI, and telemetry backends are not validated by the Python models. The E2E example covers its supplied CLI subprocess and file-backed database, not a browser or an HTTP production stack. Load and performance examples report local measurements without asserting machine-specific timing thresholds.

All 75 Advanced lessons include independent executable Python examples: 74 use the standard library, while Encryption uses cryptography and supplies isolated installation commands. All 75 examples were checked with Python 3.12.0, SQLite 3.42.0, and (for Encryption) cryptography 50.0.2 in a temporary virtual environment; project dependencies are unchanged. Distributed protocol, quorum, routing, retry, SLO, security-policy, and deployment examples are explicitly bounded models, not functioning clusters or production controls. SQLite transaction/backup examples, profiling, and AES-GCM exercise real local implementations. Synthetic arithmetic is not a measured availability, recovery, capacity, or performance guarantee.

Infrastructure as Code and Kubernetes additionally include optional real-tool exercises. They require separately installed Terraform or kubectl and, for Kubernetes, your own authorized disposable cluster. Those exercises are distinct from the offline checks; no cloud provisioning, live failover, cluster mutation, chaos injection, or production deployment is performed. Security examples never replace verified identities, maintained cryptographic libraries, trusted key services, or complete resource authorization.

All 14 Testing & Acceptance lessons include independent Python standard-library examples, checked with Python 3.12.0 and SQLite 3.42.0. Unit, Integration, Contract, Regression, and Security Test examples run unittest directly; other scripts use assertions and, where relevant, print local measurements. E2E executes the supplied tiny CLI through child processes and a temporary file-backed SQLite database. Chaos Test deliberately exits only its own disposable child workers at named transaction boundaries, then checks local recovery. No external scanning, real stress traffic, live chaos injection, or production effects are performed.

Load and performance examples report local measurements without machine-specific timing thresholds. Stress Test is explicitly a synthetic bounded-queue model, not a measured server capacity test. Acceptance Criteria demonstrates selected functional cases; UAT and FAT provide human procedures and sample report/baseline gates, not actual user sign-off, a completed supplier acceptance campaign, or certification. No extra packages or project dependency changes are required for these 14 lessons.

Authentication/authorization examples use local fixtures and intentionally omit production identity issuance, durable security infrastructure, and complete browser/login flows. Treat them as executable explanations, not deployable security systems. Security source links appear beside the relevant guidance in each lesson.

The broader task API remains an illustrative contract, not a complete supplied application. Pseudocode is framework-neutral; curl examples in lessons 1–3 require your own local implementation. The lesson 8 server implements only its documented subset.

Checklist boxes track your learning progress. Mark an item complete when you can answer its review questions and work through its practice scenarios.
