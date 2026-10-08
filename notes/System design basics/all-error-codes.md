# All Error Codes in System Design

## 1. HTTP Status Codes

### Successful Responses (2xx)
- 200 OK
- 201 Created
- 202 Accepted
- 204 No Content

### Redirection Responses (3xx)
- 300 Multiple Choices
- 301 Moved Permanently
- 302 Found
- 304 Not Modified
- 307 Temporary Redirect
- 308 Permanent Redirect

### Client Errors (4xx)
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 408 Request Timeout
- 409 Conflict
- 410 Gone
- 422 Unprocessable Entity
- 429 Too Many Requests

### Server Errors (5xx)
- 500 Internal Server Error
- 501 Not Implemented
- 502 Bad Gateway
- 503 Service Unavailable
- 504 Gateway Timeout
- 505 HTTP Version Not Supported
- 507 Insufficient Storage
- 508 Loop Detected
- 510 Not Extended
- 511 Network Authentication Required

## 2. Common Application-Level Error Codes

### Validation Errors
- E1001 Invalid input format
- E1002 Missing required field
- E1003 Invalid data type
- E1004 Value out of range
- E1005 Invalid enum value

### Authentication and Authorization Errors
- E2001 Invalid token
- E2002 Token expired
- E2003 User not authenticated
- E2004 Access denied
- E2005 Permission missing

### Resource Errors
- E3001 Resource not found
- E3002 Resource already exists
- E3003 Resource locked
- E3004 Resource exhausted
- E3005 Resource quota exceeded

### Database Errors
- E4001 Connection failure
- E4002 Timeout while querying
- E4003 Deadlock detected
- E4004 Constraint violation
- E4005 Data not found
- E4006 Duplicate entry
- E4007 Database unavailable

### Network and Integration Errors
- E5001 Connection timeout
- E5002 DNS resolution failed
- E5003 Service unreachable
- E5004 API contract mismatch
- E5005 Retry limit exceeded
- E5006 Circuit breaker open

### Business Logic Errors
- E6001 Invalid workflow state
- E6002 Operation not allowed in current state
- E6003 Payment failed
- E6004 Insufficient balance
- E6005 Duplicate transaction

### System Errors
- E7001 Internal processing error
- E7002 Dependency failure
- E7003 Cache miss / cache failure
- E7004 Queue processing failure
- E7005 Message delivery failure

## 3. Distributed System Error Codes

- ERR_TIMEOUT: request took too long
- ERR_RETRYABLE: temporary failure, retry later
- ERR_NON_RETRYABLE: permanent failure
- ERR_RATE_LIMITED: request limited by quota
- ERR_DEGRADED: service is degraded but still running
- ERR_UNAVAILABLE: service unavailable
- ERR_CONSISTENCY: data inconsistency detected
- ERR_PARTITION: network partition or split-brain scenario
- ERR_CIRCUIT_OPEN: downstream service is blocked

## 4. Typical Error Code Format

A common format is:
- 2xx = success
- 3xx = redirection
- 4xx = client-side issue
- 5xx = server-side issue
- E### = custom application error
- ERR_### = distributed system error

## 5. Notes

- Use meaningful and consistent error codes for debugging.
- Return clear error messages along with codes.
- Distinguish retryable vs non-retryable errors.
- Log error codes centrally for monitoring and incident tracking.

## 6. Summary

Error codes help developers and systems identify:
- What failed
- Why it failed
- Whether it can be retried
- Which component is responsible
- How to handle the issue correctly

This makes debugging, monitoring, and system design much more reliable.
