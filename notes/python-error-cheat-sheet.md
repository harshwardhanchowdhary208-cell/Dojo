# Python Error Cheat Sheet (Quick Revision)

Python mostly uses exceptions, not numeric error codes.

## Most common Python errors

### 1) Syntax errors
- `SyntaxError` → code is written incorrectly
  - Example: missing `:`, wrong parentheses, invalid Python
  - Fix: rewrite the code correctly
- `IndentationError` → wrong spacing/indentation
  - Fix: use consistent indentation (usually 4 spaces)
- `TabError` → mixing tabs and spaces
  - Fix: use only spaces or only tabs
- `EOFError` → unexpected end of file while reading input
  - Fix: provide the needed input

### 2) Name and variable errors
- `NameError` → variable/function not defined
  - Fix: define it before use
- `UnboundLocalError` → local variable used before assignment
  - Fix: initialize before using
- `AttributeError` → object has no such attribute
  - Fix: check object type and attribute name

### 3) Type and value errors
- `TypeError` → wrong data type
  - Example: adding string to integer
  - Fix: convert type or validate input
- `ValueError` → correct type, wrong value
  - Example: `int("abc")`
  - Fix: check the value before conversion
- `ZeroDivisionError` → division by zero
  - Fix: check if divisor is zero
- `AssertionError` → assertion condition failed
  - Fix: ensure the condition is correct

### 4) Collection errors
- `IndexError` → index out of range
  - Fix: check the length of the list
- `KeyError` → dictionary key not found
  - Fix: check whether the key exists
- `RecursionError` → too much recursion
  - Fix: add a base case or use loops

### 5) File and I/O errors
- `FileNotFoundError` → file does not exist
  - Fix: check file path
- `PermissionError` → no permission to read/write
  - Fix: change permissions or use proper access
- `OSError` → general OS/filesystem issue
  - Fix: read the error message carefully

### 6) Import errors
- `ModuleNotFoundError` → module/package is missing
  - Fix: install it with `pip install ...`
- `ImportError` → import path or dependency issue
  - Fix: fix package name or installation

### 7) Math and numeric errors
- `OverflowError` → number too big
  - Fix: limit input or use bigger data type
- `FloatingPointError` → invalid floating calculation
  - Fix: check values and use safer logic

### 8) Program flow and runtime errors
- `RuntimeError` → general runtime error
  - Fix: inspect code logic
- `KeyboardInterrupt` → user pressed Ctrl+C
  - Fix: handle gracefully if needed
- `SystemExit` → program exits intentionally
  - Fix: not usually a bug; only catch if necessary

## Common beginner-friendly examples

```python
# NameError
print(name)

# TypeError
print("2" + 3)

# ValueError
int("abc")

# ZeroDivisionError
x = 10 / 0

# IndexError
arr = [1, 2, 3]
print(arr[10])

# KeyError
d = {"a": 1}
print(d["b"])

# FileNotFoundError
open("missing.txt")
```

## How to handle errors

```python
try:
    x = int("abc")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print("Unexpected error:", e)
```

## Very short memory trick
- `SyntaxError` = code structure is wrong
- `TypeError` = wrong type
- `ValueError` = wrong value
- `IndexError` = wrong list index
- `KeyError` = wrong dictionary key
- `FileNotFoundError` = file missing
- `PermissionError` = no access
- `ImportError` / `ModuleNotFoundError` = package problem
- `ZeroDivisionError` = dividing by zero

## Common OS errno values
- `2` = `ENOENT` → no such file or directory
- `13` = `EACCES` → permission denied
- `17` = `EEXIST` → file already exists
- `22` = `EINVAL` → invalid argument

## Quick fix rule
When Python throws an error:
1. Read the error type
2. Read the message
3. Check the exact line
4. Fix the cause
5. Run again

This is the fastest way to debug Python errors.
