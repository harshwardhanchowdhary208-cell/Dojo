# Python Errors with Interview-Style Examples

## 1) What is a `SyntaxError`?
**Question:** What happens if you forget a colon in a function or loop?

```python
for i in range(5)
    print(i)
```

**Answer:** Python raises `SyntaxError` because the syntax is incomplete.

**Fix:** Add the missing colon.

```python
for i in range(5):
    print(i)
```

## 2) What is a `NameError`?
```python
print(age)
```

**Cause:** `age` was never defined.

**Fix:** Define it first.

```python
age = 25
print(age)
```

## 3) What is a `TypeError`?
```python
print("10" + 5)
```

**Cause:** You cannot add string and integer directly.

**Fix:** Convert the types.

```python
print("10" + str(5))
# or
print(int("10") + 5)
```

## 4) What is a `ValueError`?
```python
int("abc")
```

**Cause:** The value is not a valid integer string.

**Fix:** Validate the input first.

```python
text = "abc"
if text.isdigit():
    print(int(text))
else:
    print("Not a valid number")
```

## 5) What is a `ZeroDivisionError`?
```python
print(10 / 0)
```

**Cause:** Division by zero is not allowed.

**Fix:** Check the denominator.

```python
num = 10
div = 0
if div != 0:
    print(num / div)
else:
    print("Cannot divide by zero")
```

## 6) What is an `IndexError`?
```python
arr = [1, 2, 3]
print(arr[10])
```

**Cause:** Index is out of range.

**Fix:** Check list length before indexing.

```python
arr = [1, 2, 3]
if 0 <= 10 < len(arr):
    print(arr[10])
else:
    print("Index out of range")
```

## 7) What is a `KeyError`?
```python
d = {"name": "Amit"}
print(d["age"])
```

**Cause:** The key does not exist.

**Fix:** Use `.get()` or check before access.

```python
d = {"name": "Amit"}
print(d.get("age", "Not found"))
```

## 8) What is a `FileNotFoundError`?
```python
open("missing.txt")
```

**Cause:** The file path is wrong or the file does not exist.

**Fix:** Check path and existence.

```python
path = "missing.txt"
try:
    f = open(path)
except FileNotFoundError:
    print("File not found")
```

## 9) What is a `ModuleNotFoundError`?
```python
import numpy
```

**Cause:** The package is not installed.

**Fix:** Install it.

```bash
pip install numpy
```

## 10) What is a `RecursionError`?
```python
def countdown(n):
    print(n)
    countdown(n - 1)

countdown(5)
```

**Cause:** No stopping condition.

**Fix:** Add a base case.

```python
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

## Interview answer pattern
When asked about an error in an interview, answer like this:

1. State the error name
2. Explain the cause
3. Give an example
4. Explain the fix

Example:

> `TypeError` occurs when we use the wrong data type in an operation. For example, adding a string and integer raises `TypeError`. To fix it, convert the types or validate input before performing the operation.

## Most common interview errors
- `SyntaxError`
- `NameError`
- `TypeError`
- `ValueError`
- `ZeroDivisionError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`
- `ModuleNotFoundError`
- `RecursionError`

## Final interview tip
Always mention:
- the exception name
- the reason it occurs
- the fix approach

This shows strong understanding of Python debugging.
