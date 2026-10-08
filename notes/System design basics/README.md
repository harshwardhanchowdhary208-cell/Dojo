# System Design Basics

## Types of Errors Covered in System Design

### 1. Requirement Errors
- Missing or unclear requirements
- Wrong assumptions about user needs
- Confusing functional and non-functional requirements

### 2. Design Errors
- Poor architecture decisions
- Weak modularization
- Tight coupling between components
- Unclear responsibilities

### 3. Functional Errors
- Application logic does not match business requirements
- Wrong calculations or processing logic
- Incorrect validation rules

### 4. Performance Errors
- Slow response time
- High latency
- Poor query efficiency
- Insufficient resource allocation

### 5. Scalability Errors
- System fails under increased traffic
- No horizontal scaling plan
- Single bottleneck in the architecture
- Uneven workload distribution

### 6. Reliability Errors
- Frequent crashes
- Failed recovery after outages
- No failover or redundancy
- Unstable dependencies

### 7. Availability Errors
- Downtime during maintenance or failures
- Service outages due to single points of failure
- Missing backup systems
- Delayed recovery after incidents

### 8. Consistency Errors
- Different services showing different data states
- Lost updates
- Delta between database replicas
- Stale reads and out-of-sync data

### 9. Data Errors
- Duplicate or corrupted records
- Schema mismatch
- Broken migrations
- Missing data or incorrect data types

### 10. Security Errors
- SQL injection
- Cross-site scripting (XSS)
- Broken authentication
- Insecure API access
- Data leakage and weak encryption

### 11. Integration Errors
- API contract mismatches
- Message format mismatches
- Dependency version incompatibility
- Connection failures between services

### 12. Operational Errors
- Poor monitoring and logging
- No alerting system
- Slow incident response
- Lack of deployment automation

### 13. Fault Tolerance Errors
- No retry policies
- No circuit breakers
- No graceful degradation
- No fallback strategy

### 14. Network Errors
- Connection drops
- DNS issues
- Timeouts and packet loss
- TLS or reverse proxy misconfiguration

### 15. Capacity Planning Errors
- Underestimating growth
- Overprovisioning without reason
- No resource forecasting
- Poor caching strategy

### 16. Maintainability Errors
- Hard-to-read code
- No documentation
- Poor test coverage
- Difficult updates and debugging

### 17. Cost Errors
- Overuse of expensive cloud services
- Poor optimization of storage and compute
- Excessive resource usage

### 18. User Experience Errors
- Poor feedback to users
- Long waiting times
- Unclear failure messages
- Broken workflows from backend issues

## Final Idea
A strong system design should minimize these errors by balancing:
- Correctness
- Performance
- Scalability
- Reliability
- Security
- Maintainability
- Cost efficiency

The goal is to build a system that works properly, stays available, handles growth, and remains easy to operate and maintain.
