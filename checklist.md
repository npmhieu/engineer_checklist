# Backend / Software Developer Knowledge Checklist — v1

## 1. Basic / Fundamental

### API & Application
- [ ] HTTP Fundamentals
- [ ] API / Request-Response
- [ ] REST API
- [ ] CRUD Resource
- [ ] Request Validation
- [ ] Business Validation
- [ ] Error Handling
- [ ] HTTP Status Codes
- [ ] Search / Filter / Sort
- [ ] Pagination
- [ ] API Versioning
- [ ] Idempotency Basics

### Authentication & Authorization
- [ ] Authentication
- [ ] Authorization
- [ ] User Management
- [ ] Role-Based Access Control (RBAC)
- [ ] Session / Token
- [ ] JWT Basics
- [ ] Password / Credential Security

### Database
- [ ] Database Fundamentals
- [ ] Schema / Data Modeling
- [ ] Relationships
- [ ] Normalization
- [ ] Primary / Foreign Key
- [ ] Indexes
- [ ] Basic Query Optimization
- [ ] Transactions
- [ ] Migration Basics

### Common Features
- [ ] File Upload
- [ ] File Storage
- [ ] Notifications
- [ ] Export / Import
- [ ] Audit Log
- [ ] Reporting / Analytics

### Architecture & Code Organization
- [ ] Monolithic Architecture
- [ ] Layered Architecture
- [ ] Separation of Concerns
- [ ] Package / Folder Organization
- [ ] Dependency Direction
- [ ] API / Worker / Cron Separation

### Testing
- [ ] Unit Test
- [ ] Integration Test

### Development & Operations
- [ ] Git
- [ ] Environment / Configuration
- [ ] Logging
- [ ] Health Check
- [ ] Basic Monitoring
- [ ] Basic CI/CD


## 2. Intermediate

### API & Application
- [ ] Advanced API Design
- [ ] Backward Compatibility
- [ ] API Contract
- [ ] Advanced Idempotency
- [ ] Rate Limiting
- [ ] Webhook
- [ ] Third-party API Integration
- [ ] Service-to-Service Communication

### Database & Performance
- [ ] Advanced Transactions
- [ ] Concurrency
- [ ] Race Conditions
- [ ] Optimistic Locking
- [ ] Pessimistic Locking
- [ ] Query Optimization
- [ ] Database Migration in Production
- [ ] Caching
- [ ] Redis
- [ ] Connection Pooling

### Async / Background Processing
- [ ] Background Task
- [ ] Job
- [ ] Message
- [ ] Producer
- [ ] Message Queue
- [ ] Consumer
- [ ] Worker
- [ ] Cronjob
- [ ] Event
- [ ] Event-Driven Architecture
- [ ] Queue vs Topic
- [ ] Job Status / Lifecycle
- [ ] Retry
- [ ] Exponential Backoff
- [ ] Timeout
- [ ] Dead Letter Queue (DLQ)
- [ ] Duplicate Processing
- [ ] Idempotent Consumer

### Application Features
- [ ] Async Export / Import
- [ ] Notification Architecture
- [ ] Audit / Activity History
- [ ] Reporting Architecture
- [ ] Batch Processing

### Architecture
- [ ] Feature / Domain-oriented Architecture
- [ ] Modular Monolith
- [ ] DDD Basics
- [ ] Bounded Context
- [ ] Domain Service
- [ ] Application Service
- [ ] Infrastructure Layer
- [ ] Hybrid Architecture
- [ ] Shared Platform / Infrastructure

### Testing
- [ ] End-to-End (E2E) Test
- [ ] Contract Test
- [ ] Regression Test
- [ ] Smoke Test
- [ ] Load Test
- [ ] Basic Performance Test

### Observability
- [ ] Structured Logging
- [ ] Metrics
- [ ] Error Tracking
- [ ] Monitoring
- [ ] Alerting
- [ ] Request ID
- [ ] Correlation ID
- [ ] Distributed Tracing

### Deployment
- [ ] Docker / Containers
- [ ] CI/CD Pipeline
- [ ] Production Deployment
- [ ] Database Migration Strategy
- [ ] Rollback
- [ ] Feature Flags


## 3. Advanced

### Distributed Systems
- [ ] Distributed Systems Fundamentals
- [ ] Service Boundaries
- [ ] Microservices Architecture
- [ ] Inter-service Communication
- [ ] Event-Driven Architecture at Scale
- [ ] Event Schema / Versioning
- [ ] Event Ordering
- [ ] Event Replay
- [ ] Fan-out
- [ ] Consumer Groups

### Messaging
- [ ] Message Delivery Semantics
- [ ] At-most-once Delivery
- [ ] At-least-once Delivery
- [ ] Effectively-once Processing
- [ ] Exactly-once Concepts
- [ ] Message Ordering
- [ ] Poison Messages
- [ ] Advanced Retry Strategies
- [ ] Dead Letter Queue Strategy
- [ ] Queue Backpressure

### Distributed Consistency
- [ ] Eventual Consistency
- [ ] Strong Consistency
- [ ] CAP Theorem
- [ ] Distributed Transactions
- [ ] Saga Pattern
- [ ] Compensation
- [ ] Distributed Locking
- [ ] Distributed Idempotency

### Database / Scaling
- [ ] Replication
- [ ] Read Replicas
- [ ] Database Failover
- [ ] Partitioning
- [ ] Sharding
- [ ] Consistency Models
- [ ] Large-scale Data Architecture

### Reliability
- [ ] Circuit Breaker
- [ ] Bulkhead
- [ ] Graceful Degradation
- [ ] Fault Tolerance
- [ ] High Availability
- [ ] Failover
- [ ] Disaster Recovery
- [ ] Backup / Restore
- [ ] Recovery Point Objective (RPO)
- [ ] Recovery Time Objective (RTO)
- [ ] Multi-Region Architecture

### Performance
- [ ] Performance Engineering
- [ ] Profiling
- [ ] Capacity Planning
- [ ] Bottleneck Analysis
- [ ] Throughput Optimization
- [ ] Latency Optimization
- [ ] Large-scale Caching

### Observability / Operations
- [ ] Advanced Distributed Tracing
- [ ] Service Level Objectives (SLO)
- [ ] Service Level Agreements (SLA)
- [ ] Error Budget
- [ ] Capacity Monitoring
- [ ] Advanced Alerting
- [ ] Chaos Testing

### Security
- [ ] Security Architecture
- [ ] Threat Modeling
- [ ] Secrets Management
- [ ] Encryption
- [ ] Key Management
- [ ] Advanced API Security
- [ ] Zero Trust Concepts
- [ ] Dependency / Supply-chain Security

### DevOps / Delivery
- [ ] Infrastructure as Code
- [ ] Blue-Green Deployment
- [ ] Canary Deployment
- [ ] Progressive Delivery
- [ ] Advanced Feature Flags
- [ ] Kubernetes
- [ ] Multi-environment Deployment


## 4. Testing & Acceptance

### Automated Testing
- [ ] Unit Test
- [ ] Integration Test
- [ ] Contract Test
- [ ] E2E Test
- [ ] Regression Test
- [ ] Smoke Test
- [ ] Load Test
- [ ] Stress Test
- [ ] Performance Test
- [ ] Security Test
- [ ] Chaos Test

### Acceptance
- [ ] Acceptance Criteria
- [ ] User Acceptance Testing (UAT)
- [ ] Factory Acceptance Testing (FAT)


## 5. Typical Backend Flows

### 5.1 Synchronous API

The API processes the request and returns the result in the same request-response cycle.

```text
Client
  |
  v
API
  |
  v
Business Logic
  |
  v
Database / External Service
  |
  v
HTTP Response
```

### 5.2 API Triggering a Background Task

The API accepts the request, enqueues a job, and returns without waiting for the job to finish.

```text
Client
  |
  | POST /jobs
  v
API
  |
  | Enqueue job
  v
Message Queue
  |
  | API returns job ID independently
  v
Client receives 202 Accepted + job ID

Message Queue
  |
  v
Consumer / Worker
  |
  v
Background Task
  |
  v
Save Result / Job Status
```

The frontend can retrieve the result through:
- [ ] Polling
- [ ] WebSocket
- [ ] Server-Sent Events (SSE)
- [ ] Notification

### 5.3 Cronjob Triggering Background Processing

A Cronjob can execute work directly or enqueue jobs for workers.

```text
Cronjob / Scheduler
  |
  | Create or enqueue jobs
  v
Message Queue
  |
  v
Consumer / Worker
  |
  v
Background Task
  |
  v
Save Result
```

### 5.4 Event-Driven Processing

An event announces that something happened. Consumers can react to the event independently.

```text
Producer
  |
  v
Event / Message
  |
  v
Queue / Message Broker
  |
  v
Consumer / Worker
  |
  v
Event Handler / Background Task
  |
  v
Save Result or Trigger Another Event
```


## 6. Architecture Mental Model

### 6.1 Work Triggers

- API: request-driven
- Cronjob: time-driven
- Event: event-driven

### 6.2 Async Processing Components

- Message: information or work being transmitted
- Queue: stores pending messages or jobs
- Producer: publishes messages
- Consumer: receives messages
- Worker: process that consumes and executes jobs
- Background Task: work performed outside the foreground flow
- Result: outcome of processing, such as success, failure, or generated data

### 6.3 Combined Flow

API, Cronjob, and Event are alternative triggers. They do not necessarily execute one after another.

```text
                 TRIGGERS
                    |
          +---------+---------+
          |         |         |
          v         v         v
         API      Cronjob    Event
          |         |         |
          |         |         |
          v         v         v
       Direct     Job /     Event /
       Response   Message   Message
          |         |         |
          |         +----+----+
          |              |
          |              v
          |            Queue
          |              |
          |              v
          |       Consumer / Worker
          |              |
          |              v
          |       Background Task
          |              |
          |              v
          |        Result / Status
          |
          v
    HTTP Response
```

An API can either process work synchronously or enqueue work asynchronously. Cronjobs and events can also execute work directly, without a queue, when that fits the requirements.

### Key Distinctions

- API / Cronjob / Event = ways work can be triggered
- Message / Job = information or a unit of work
- Queue / Broker = transports or buffers messages
- Producer = sends messages
- Consumer = receives messages
- Worker = process that executes background jobs
- Background Task = the actual work performed asynchronously
- Result / Status = the outcome that can be stored or exposed to the client