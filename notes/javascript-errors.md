# JavaScript Errors: Causes and Fixes

JavaScript does not have a finite list of every possible error message. Programs and libraries can define custom errors, and browsers and Node.js add environment-specific errors. This guide covers the built-in ECMAScript error types and common errors you are likely to encounter.

## Built-in JavaScript error types

| Error type | Common cause | Typical fix |
|---|---|---|
| `Error` | A general error is created or thrown, often by application code | Read the message and stack trace; fix the condition that caused it |
| `AggregateError` | Several errors are grouped into one, such as when all promises passed to `Promise.any()` reject | Inspect its `errors` property and handle each underlying error |
| `EvalError` | A legacy error associated with `eval()`; modern JavaScript engines rarely throw it | Avoid `eval()`; use safer parsing or explicit logic |
| `RangeError` | A value is outside the range supported by an operation | Check bounds and input sizes |
| `ReferenceError` | A name is not available in the current scope, or a lexical variable is accessed before initialization | Declare the variable, check spelling and scope, and initialize before use |
| `SyntaxError` | Source code or parsed text is not valid JavaScript | Fix the reported syntax; for JSON, ensure the text is valid JSON |
| `TypeError` | An operation receives an incompatible value or tries an invalid operation on a value | Check the value and its type before using it |
| `URIError` | A URI encoding/decoding function receives malformed URI data | Encode/decode the correct component and validate the input |

All built-in error types inherit from `Error`. `EvalError` and `URIError` remain part of the language, although they are uncommon in everyday code.

### Examples of built-in errors

```javascript
// ReferenceError: misspelled or undeclared name
console.log(userNmae);

// TypeError: calling a value that is not a function
const value = 42;
value();

// RangeError: invalid array length
new Array(-1);

// SyntaxError: invalid JSON text
JSON.parse("{ name: 'Asha' }");

// URIError: malformed percent escape
decodeURIComponent("%");

// AggregateError: Promise.any rejects when every promise rejects
Promise.any([
  Promise.reject(new Error("First failed")),
  Promise.reject(new Error("Second failed")),
]).catch((error) => {
  if (error instanceof AggregateError) {
    console.log(error.errors);
  }
});
```

## Common JavaScript mistakes and their errors

### `ReferenceError`: variable is not defined

```javascript
console.log(total);
```

**Cause:** `total` was never declared, is misspelled, or is outside the current scope.

**Fix:** Declare the variable and check its spelling and scope.

```javascript
const total = 10;
console.log(total);
```

Accessing a `let` or `const` variable before its declaration is initialized also causes a `ReferenceError` because of the temporal dead zone.

### `TypeError`: property access on `null` or `undefined`

```javascript
const user = null;
console.log(user.name);
```

**Cause:** The value is `null` or `undefined`, so the requested property cannot be read.

**Fix:** Ensure a value exists or use optional chaining when absence is expected.

```javascript
console.log(user?.name);
```

Optional chaining is not a substitute for validating data when the value is required.

### `TypeError`: value is not callable

```javascript
const greet = "hello";
greet();
```

**Cause:** A value that is not a function was called, or a method name was misspelled.

**Fix:** Check the value and confirm the function exists before calling it.

### `TypeError`: assignment to a constant

```javascript
const count = 1;
count = 2;
```

**Cause:** A `const` binding cannot be reassigned.

**Fix:** Use `let` if the binding must be reassigned. A `const` object or array can still have its contents changed; `const` prevents rebinding, not mutation.

### `TypeError`: mixing incompatible types

```javascript
const result = 1n + 1;
```

**Cause:** Some operations, such as arithmetic between a `BigInt` and a `Number`, require compatible types.

**Fix:** Convert deliberately to a compatible type, while considering precision and range.

### `SyntaxError`: invalid syntax or JSON

```javascript
const settings = { theme: "dark" // missing closing brace
```

**Cause:** JavaScript source or text being parsed has invalid syntax.

**Fix:** Check punctuation, brackets, quotes, and the line/column in the error. JSON requires quoted property names and double-quoted strings:

```javascript
const settings = JSON.parse('{"theme":"dark"}');
```

### `RangeError`: invalid range or recursion limit

**Cause:** A number or size is outside the allowed range, such as an invalid array length, or recursion exceeds the engine's limit.

**Fix:** Validate bounds and add a stopping condition to recursive functions; use iteration for very deep work.

### `URIError`: malformed URI component

**Cause:** A URI decode function receives malformed percent-encoded text.

**Fix:** Encode data using the matching URI function and handle invalid input.

## Promise and asynchronous errors

- **Unhandled promise rejection:** A promise rejects without a rejection handler. Add `.catch(...)` or use `try`/`catch` with `await`.
- **Async error not caught:** A `try`/`catch` around an asynchronous call only catches it if the promise is awaited (or its rejection is otherwise handled).
- **`Promise.any()` rejection:** If every input promise rejects, it rejects with an `AggregateError`; inspect `error.errors`.
- **Callback errors:** A `try`/`catch` does not catch an exception thrown later in an unrelated callback. Handle errors in the callback or promise chain where they occur.

```javascript
async function loadData() {
  try {
    const response = await fetch("/api/data");
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Could not load data:", error);
    throw error;
  }
}
```

`fetch()` generally rejects for network-level failures, but not just because the server returned an HTTP error status such as 404. Check `response.ok` or `response.status`.

## Browser errors and messages

Browser developer tools may show messages that are not built-in JavaScript exception types:

- **`Uncaught ...`** means an exception was thrown without being handled at that point.
- **CORS errors** mean the browser blocked a cross-origin request under its security rules. Configure the server's CORS response; client-side JavaScript cannot override the browser's policy.
- **Network errors** can be caused by connectivity, DNS, TLS, extensions, or server failures. Check the Network panel and server logs.
- **Resource load errors** can indicate a missing or inaccessible script, image, stylesheet, or other resource. Check the URL, response status, and permissions.

The exact wording varies by browser. Use the console stack trace and Network panel to locate the cause.

## Common Node.js errors

Node.js uses standard JavaScript exceptions and also reports system errors with a `code` property. Common examples include:

| Code or error | Meaning | Typical fix |
|---|---|---|
| `ERR_MODULE_NOT_FOUND` / `MODULE_NOT_FOUND` | An imported or required module could not be found | Check the package name, installation, and import path |
| `ENOENT` | A file or directory does not exist | Check the path and working directory |
| `EACCES` / `EPERM` | The operation is not permitted | Check file permissions and operating-system access |
| `EADDRINUSE` | A requested network address or port is already in use | Stop the conflicting service or choose an available port |
| `ECONNREFUSED` | A connection was refused by the target | Check that the service is running and the host/port are correct |
| `ETIMEDOUT` | A connection or operation timed out | Check network/service health and configure a suitable timeout |

Node.js codes depend on the operation, operating system, and runtime version. Inspect `error.code`, `error.message`, and the stack trace rather than assuming every system error has the same code.

## Handling errors

Catch errors you can meaningfully recover from. Prefer specific checks and useful messages; do not silently swallow failures.

```javascript
try {
  const data = JSON.parse(input);
  console.log(data);
} catch (error) {
  if (error instanceof SyntaxError) {
    console.error("Input is not valid JSON:", error.message);
  } else {
    throw error;
  }
}
```

### Throwing a custom error

Use a built-in error type when it fits, or define a named subclass for an application-specific problem.

```javascript
class InvalidAgeError extends Error {
  constructor(message) {
    super(message);
    this.name = "InvalidAgeError";
  }
}

function validateAge(age) {
  if (!Number.isInteger(age) || age < 0) {
    throw new InvalidAgeError("Age must be a non-negative integer.");
  }
}
```

## Quick revision

- `SyntaxError` = invalid code or parsed text
- `ReferenceError` = unavailable or undeclared name
- `TypeError` = invalid operation for a value's type
- `RangeError` = value outside an allowed range
- `URIError` = malformed URI encoding/decoding input
- `AggregateError` = multiple errors collected together
- `Error` = general-purpose error
- Browser CORS/network messages and Node.js system codes are environment-specific, not additional ECMAScript error classes

## Debugging checklist

1. Read the error name and message.
2. Find the first relevant line in the stack trace.
3. Inspect the values and types used on that line.
4. Check asynchronous rejections and external resources.
5. Fix the cause, then reproduce the scenario to verify the fix.
