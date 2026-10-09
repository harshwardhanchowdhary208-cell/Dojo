# Python Error One-Page Summary

## 1. What are Python errors?
Python mostly uses exceptions, not numeric error codes.

An exception is an object that stops normal execution and tells you what went wrong.

## 2. Most important Python exceptions

### Syntax and parsing
- `SyntaxError` → invalid Python syntax
- `IndentationError` → bad indentation
- `TabError` → mixing tabs and spaces
- `EOFError` → input ended unexpectedly

### Variables and names
- `NameError` → variable/function not defined
- `UnboundLocalError` → local variable used before assignment
- `AttributeError` → attribute not found

### Types and values
- `TypeError` → wrong data type
- `ValueError` → correct type, invalid value
- `ZeroDivisionError` → division by zero
- `AssertionError` → assertion condition failed

### Collections
- `IndexError` → index out of range
- `KeyError` → dictionary key missing
- `RecursionError` → too much recursion

### Files and input/output
- `FileNotFoundError` → file missing
- `PermissionError` → no access
- `OSError` → general operating system/file problem
- `IOError` → old I/O exception name

### Imports and modules
- `ModuleNotFoundError` → module/package missing
- `ImportError` → import problem or dependency issue

### Runtime and logic
- `RuntimeError` → general runtime error
- `KeyboardInterrupt` → user pressed Ctrl+C
- `SystemExit` → program exits intentionally

## 3. Quick meaning table

| Error | Meaning | Fix |
|---|---|---|
| `SyntaxError` | Code is invalid | Correct code syntax |
| `NameError` | Variable missing | Define it first |
| `TypeError` | Wrong type | Convert/check type |
| `ValueError` | Wrong value | Validate input |
| `ZeroDivisionError` | Dividing by zero | Check divisor |
| `IndexError` | Bad list index | Check length |
| `KeyError` | Bad dict key | Check key exists |
| `FileNotFoundError` | File missing | Check path |
| `PermissionError` | No access | Fix permissions |
| `ImportError` | Import failed | Install/fix module |

## 4. Example errors

```python
# NameError
print(name)

# TypeError
print("5" + 5)

# ValueError
int("abc")

# ZeroDivisionError
x = 10 / 0

# IndexError
nums = [1, 2, 3]
print(nums[99])

# KeyError
person = {"name": "Amit"}
print(person["age"])

# FileNotFoundError
open("missing.txt")
```

## 5. Handling errors safely

```python
try:
    num = int("hello")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("This runs no matter what.")
```

## 6. Best practices
- Read the error type first
- Read the message carefully
- Check the exact line mentioned
- Validate input and file paths
- Catch specific exceptions, not everything
- Use `try/except` for risky operations

## 7. Common OS errno values
- `2` = `ENOENT` → file/folder not found
- `13` = `EACCES` → permission denied
- `17` = `EEXIST` → file already exists
- `22` = `EINVAL` → invalid argument

## 8. Simple rule for debugging
1. Read the exception name
2. Check the exact line
3. Understand the cause
4. Fix it
5. Run again

This is the fastest and most reliable way to debug Python errors.
