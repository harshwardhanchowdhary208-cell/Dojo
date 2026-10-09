# Python Error Codes, Exceptions, Causes, and Fixes

Python does not normally use numeric "error codes" the way C or OS APIs do. In Python, most errors are exceptions with names such as `SyntaxError`, `ValueError`, `TypeError`, etc. Some lower-level OS errors also carry `errno` numbers such as `2` for file not found and `13` for permission denied.

## 1) Syntax and parsing errors

| Error | Cause | Fix |
|---|---|---|
| `SyntaxError` | The code breaks Python grammar; example: missing colon, bad parentheses, invalid syntax | Correct the syntax and check for missing `:`, quotes, or brackets |
| `IndentationError` | Wrong indentation or inconsistent spaces/tabs | Use consistent indentation (usually 4 spaces) |
| `TabError` | Mixing tabs and spaces in indentation | Replace tabs with spaces or normalize indentation |
| `UnicodeError` | Invalid Unicode encoding or decoding | Use correct text encoding like `utf-8` and handle encoding errors |
| `EOFError` | End of file reached while reading input unexpectedly | Provide input data or handle missing input gracefully |

## 2) Variable and name issues

| Error | Cause | Fix |
|---|---|---|
| `NameError` | Variable, function, or class is not defined | Check spelling and scope; define it before use |
| `UnboundLocalError` | Local variable is referenced before assignment | Initialize the variable before use |
| `AttributeError` | Object has no such attribute | Check type and attribute names |
| `ModuleNotFoundError` | Module is not installed or import path is wrong | Install with `pip install ...` or fix the import path |
| `ImportError` | A module import fails for some reason other than not being installed | Fix the module name, package structure, or dependency |

## 3) Type and value problems

| Error | Cause | Fix |
|---|---|---|
| `TypeError` | Wrong data type is used in an operation | Convert values to the correct type or validate input |
| `ValueError` | Correct type but invalid value | Validate value before using it |
| `ZeroDivisionError` | Division by zero | Check the divisor before dividing |
| `OverflowError` | Numeric result is too large | Use a larger numeric type or limit the input |
| `FloatingPointError` | Floating-point arithmetic problem | Check input values and use safe numeric logic |
| `AssertionError` | An assertion condition failed | Check the logic of the assertion and code conditions |

## 4) Collection and sequence errors

| Error | Cause | Fix |
|---|---|---|
| `IndexError` | Index is out of range | Check collection length before indexing |
| `KeyError` | Dictionary key does not exist | Use `dict.get()` or verify the key exists |
| `MemoryError` | Not enough memory for the operation | Reduce data size or optimize memory usage |
| `RecursionError` | Function calls itself too deeply | Add a stopping condition or use an iterative solution |

## 5) File and I/O errors

| Error | Cause | Fix |
|---|---|---|
| `FileNotFoundError` | File does not exist | Check the path and ensure the file exists |
| `PermissionError` | The program lacks permission to read/write the file | Fix file permissions or run with the required access |
| `IsADirectoryError` | A directory path was used as if it were a file | Use the correct file path or directory handling |
| `NotADirectoryError` | A file path was used where a directory was expected | Correct the path structure |
| `OSError` | Generic operating system or filesystem error | Read the message and handle the specific OS error |
| `IOError` | Older name for I/O-related errors | Use `OSError` in modern Python |
| `BlockingIOError` | A non-blocking I/O operation would block | Use async or correct I/O strategy |
| `ConnectionError` | Network connection fails | Check server status, port, and connectivity |
| `TimeoutError` | Operation exceeded a time limit | Increase timeout or optimize the operation |

## 6) Iteration and loop errors

| Error | Cause | Fix |
|---|---|---|
| `StopIteration` | Iterator is exhausted | Handle iteration boundaries correctly |
| `RuntimeError` | Generic runtime failure | Inspect the exception message and fix underlying logic |
| `GeneratorExit` | Generator is closed | Avoid forcibly exiting generators during normal program flow |
| `StopAsyncIteration` | Async iterator is exhausted | Handle async iteration properly |

## 7) Program control and logic flow

| Error | Cause | Fix |
|---|---|---|
| `KeyboardInterrupt` | User pressed Ctrl+C or Ctrl+Break | Handle interrupts intentionally or exit cleanly |
| `SystemExit` | Program calls `sys.exit()` | Catch only if necessary, otherwise let the program exit |
| `BrokenPipeError` | Writing to a closed pipe or socket | Handle pipe/socket cleanup and retries |
| `ChildProcessError` | Child process operation failed | Check the subprocess call and system state |
| `ProcessLookupError` | Process could not be found | Check the process ID and lifecycle |
| `NotImplementedError` | Method or class is not implemented yet | Complete the implementation or subclass correctly |

## 8) Numeric and math errors

| Error | Cause | Fix |
|---|---|---|
| `ArithmeticError` | Base class for math-related errors | Catch specific numeric exceptions instead of the broad base |
| `OverflowError` | Numeric overflow occurs | Use larger numeric types or validation |
| `ZeroDivisionError` | Division by zero | Validate the denominator before calculating |
| `FloatingPointError` | Invalid floating point arithmetic | Check inputs and use safer numeric logic |

## 9) Custom and user-defined exceptions

| Error | Cause | Fix |
|---|---|---|
| `Exception` | Base class for most Python exceptions | Use custom subclasses for domain-specific errors |
| Custom exception classes | Your own application raises a custom problem | Raise meaningful messages and handle them specifically |

## 10) Warnings (not always fatal, but important)

These are not usually fatal but should not be ignored.

| Warning | Cause | Fix |
|---|---|---|
| `Warning` | Base class for warnings | Review code quality issues |
| `DeprecationWarning` | Feature is deprecated | Update code to supported APIs |
| `PendingDeprecationWarning` | Feature will be deprecated soon | Migrate before the future release |
| `SyntaxWarning` | Possible syntax issue | Fix the code pattern |
| `RuntimeWarning` | Suspicious runtime behavior | Review logic and assumptions |
| `UserWarning` | User defined warning | Use it for specific user-facing alerts |
| `ResourceWarning` | Resource was not properly cleaned up | Close files, sockets, DB connections, etc. |
| `FutureWarning` | A behavior change is expected in a future version | Update the code to avoid future breakage |

## Built-in exception hierarchy in Python

```python
BaseException
├── Exception
│   ├── ArithmeticError
│   │   ├── OverflowError
│   │   ├── ZeroDivisionError
│   │   └── FloatingPointError
│   ├── AssertionError
│   ├── AttributeError
│   ├── ImportError
│   ├── IndexError
│   ├── KeyError
│   ├── MemoryError
│   ├── NameError
│   ├── OSError
│   │   ├── FileNotFoundError
│   │   ├── PermissionError
│   │   ├── IsADirectoryError
│   │   └── NotADirectoryError
│   ├── RecursionError
│   ├── RuntimeError
│   ├── SyntaxError
│   ├── TypeError
│   ├── ValueError
│   └── UnicodeError
├── KeyboardInterrupt
├── SystemExit
└── GeneratorExit
```

## How to handle errors in Python

Use `try`, `except`, and `finally` blocks:

```python
try:
    value = int("abc")
except ValueError:
    print("Input is not a valid integer.")
except TypeError:
    print("Wrong type.")
else:
    print("Success")
finally:
    print("This always runs")
```

## Best practices

- Catch the most specific exception first
- Do not catch everything unless absolutely necessary
- Log the actual error message
- Validate user input before processing
- Check file paths and permission issues
- Use `raise` and custom exceptions for cleaner application logic

## Common OS-level numeric error codes (`errno`)

Python normally uses names, but some OS operations return numeric `errno` values. Examples:

| Number | Name | Meaning |
|---|---|---|
| `2` | `ENOENT` | No such file or directory |
| `13` | `EACCES` | Permission denied |
| `9` | `EBADF` | Bad file descriptor |
| `17` | `EEXIST` | File already exists |
| `22` | `EINVAL` | Invalid argument |
| `28` | `ENOSPC` | No space left on device |

Example:

```python
import errno

print(errno.ENOENT)
print(errno.EACCES)
```

## Summary

Python errors are mostly exceptions, not numeric codes. The important idea is:

- `SyntaxError` = wrong code structure
- `NameError` = missing variable/function
- `TypeError` = wrong type
- `ValueError` = wrong value
- `IndexError` / `KeyError` = invalid collection access
- `FileNotFoundError` / `PermissionError` = file issues
- `ZeroDivisionError` = division by zero
- `ImportError` / `ModuleNotFoundError` = import problems
- `RecursionError` = infinite recursion

If you understand the error type, the cause is usually obvious and the fix is straightforward.
