# Python Interview Questions and Answers

## Python basics

### 1. What is Python?
Python is a high-level, general-purpose programming language. It is known for readable syntax and has a large standard library and ecosystem.

### 2. Is Python compiled or interpreted?
Python is commonly described as interpreted. In CPython, source code is first compiled to bytecode, which the Python virtual machine executes.

### 3. What are Python's key features?
- Readable, concise syntax
- Dynamic typing
- Automatic memory management
- Support for procedural, object-oriented, and functional programming
- A large standard library and third-party package ecosystem

### 4. What is the difference between a list and a tuple?
A list is mutable; a tuple is immutable. Both are ordered sequences and can contain values of different types.

```python
items = [1, 2, 3]
items[0] = 10

point = (4, 5)
# point[0] = 10  # TypeError: tuples do not support item assignment
```

### 5. What is the difference between a set and a dictionary?
A set stores unique values. A dictionary stores key-value pairs with unique keys.

```python
unique_ids = {1, 2, 3}
user = {"name": "Asha", "active": True}
```

### 6. What does mutable versus immutable mean?
Mutable objects can be changed after creation; immutable objects cannot. Lists and dictionaries are mutable. Integers, strings, and tuples are immutable.

### 7. What is `None`?
`None` is Python's singleton value for representing the absence of a value. Compare it using identity:

```python
result = None
if result is None:
    print("No result")
```

### 8. What is the difference between `==` and `is`?
`==` compares values for equality. `is` checks whether two references point to the same object. Use `is None` when checking for `None`.

### 9. What are truthy and falsy values?
Values such as `False`, `None`, numeric zero, and empty collections are falsy. Most other values are truthy. Custom classes can define truthiness with `__bool__` or `__len__`.

### 10. What is a variable in Python?
A variable is a name bound to an object. Python variables do not have fixed declared types; the object has a type.

## Functions and language features

### 11. What are `*args` and `**kwargs`?
`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

```python
def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(1, 2, name="Asha")
```

### 12. What is a lambda function?
A lambda is a small anonymous function consisting of a single expression.

```python
square = lambda number: number * number
```

For complex logic, use a regular `def` function.

### 13. What is a list comprehension?
A concise way to create a list from an iterable, optionally filtering values.

```python
squares = [number * number for number in range(5)]
```

### 14. What is a generator?
A generator produces values lazily, one at a time, using `yield`. It can reduce memory use when processing large sequences.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1
```

### 15. What is an iterator?
An iterator produces values one at a time through `__next__()` and signals completion with `StopIteration`. `iter(value)` obtains an iterator from an iterable.

### 16. What is the difference between an iterable and an iterator?
An iterable can provide an iterator, usually through `__iter__()`. An iterator keeps iteration state and provides the next item with `__next__()`.

### 17. What is a decorator?
A decorator wraps or modifies a function or class, commonly to add reusable behavior such as logging or access checks.

```python
def announce(function):
    def wrapper():
        print("Starting")
        return function()
    return wrapper
```

For production decorators, `functools.wraps` helps preserve the wrapped function's metadata.

### 18. What is a closure?
A closure is a function that retains access to variables from its enclosing scope, even after that enclosing function has returned.

### 19. What is a namespace?
A namespace maps names to objects. Python has local, enclosing, global, and built-in scopes; name lookup follows the LEGB order.

### 20. What is the difference between `global` and `nonlocal`?
`global` refers to a name in the module-level scope. `nonlocal` refers to a name in the nearest enclosing function scope.

## Object-oriented programming

### 21. What is a class and what is an object?
A class defines a type and its behavior. An object is an instance of a class.

### 22. What does `self` mean?
`self` is the conventional name for the instance passed to an instance method. It lets the method access that instance's attributes and other methods.

### 23. What is inheritance?
Inheritance lets a class derive behavior from another class. The child class can reuse or override parent behavior.

### 24. What is method overriding?
Overriding occurs when a subclass provides its own implementation of a method defined by its parent class.

### 25. What is the difference between an instance method, class method, and static method?
- An instance method receives the instance as `self`.
- A class method receives the class as `cls` and is declared with `@classmethod`.
- A static method receives neither automatically and is declared with `@staticmethod`.

### 26. What is encapsulation?
Encapsulation groups data and behavior together and provides a controlled interface. Python uses naming conventions such as `_internal`; a leading double underscore triggers name mangling, not strict privacy.

### 27. What is polymorphism?
Polymorphism lets different objects be used through a common interface. In Python, this often works through duck typing: an object is suitable if it supports the needed operations.

### 28. What are dunder methods?
Dunder (double-underscore) methods are special methods, such as `__init__`, `__repr__`, and `__len__`, that define how objects work with Python language operations.

## Errors and exception handling

### 29. What is the difference between a syntax error and an exception?
A syntax error means Python cannot parse the code. An exception occurs while syntactically valid code is running.

### 30. What is the difference between `TypeError` and `ValueError`?
`TypeError` means an operation received an inappropriate type. `ValueError` means the type is acceptable but the value is inappropriate.

```python
"age" + 5       # TypeError: incompatible operand types
int("not a number")  # ValueError: string cannot represent an integer
```

### 31. How do you handle exceptions?
Use `try` for risky code and catch specific exceptions with `except`. Use `else` for code that should run when no exception occurs and `finally` for cleanup.

```python
try:
    age = int(user_input)
except ValueError:
    print("Enter a whole number.")
else:
    print(f"Age: {age}")
```

### 32. How do you raise an exception?
Use `raise` when a function cannot complete its contract or a condition is invalid.

```python
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("amount must not be negative")
    return balance - amount
```

### 33. Should you catch `Exception`?
Catch the most specific exception that you can handle. Catching `Exception` broadly can hide programming errors; use it only at a boundary where you can report or recover appropriately.

### 34. How do you define a custom exception?
Subclass `Exception` and give the exception a descriptive name.

```python
class InsufficientFundsError(Exception):
    pass
```

## Common practical questions

### 35. What is the difference between `append()` and `extend()`?
`append(value)` adds one item to a list. `extend(iterable)` adds each item from an iterable.

```python
values = [1, 2]
values.append([3, 4])  # [1, 2, [3, 4]]
values.extend([5, 6])  # [1, 2, [3, 4], 5, 6]
```

### 36. What is the difference between `sort()` and `sorted()`?
`list.sort()` sorts a list in place and returns `None`. `sorted(iterable)` returns a new sorted list and leaves the original iterable unchanged.

### 37. What is the difference between shallow and deep copy?
A shallow copy creates a new outer container but keeps references to nested objects. A deep copy recursively copies nested objects. Use `copy.copy()` or `copy.deepcopy()` when appropriate.

### 38. Why should mutable default arguments be avoided?
Default argument expressions are evaluated once when the function is defined, so a mutable default can be shared across calls.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 39. What is a context manager?
A context manager handles setup and cleanup around a block of code. The `with` statement is commonly used to ensure files or other resources are closed.

```python
with open("notes.txt", encoding="utf-8") as file:
    contents = file.read()
```

### 40. What is PEP 8?
PEP 8 is Python's style guide. It recommends conventions for readable, consistent Python code, including naming and formatting.

### 41. What is a virtual environment?
A virtual environment isolates a project's installed packages from other projects and the system Python installation. Create one with `python -m venv .venv`.

### 42. What is `pip`?
`pip` is a package installer commonly used to install and manage Python packages from package indexes.

### 43. What is the GIL?
In standard CPython builds, the Global Interpreter Lock (GIL) allows only one thread at a time to execute Python bytecode in a process. Threads can still help with I/O-bound work; multiprocessing can help with CPU-bound work. Python implementations and newer free-threaded builds may differ.

### 44. What is the difference between threading and multiprocessing?
Threading uses multiple threads within one process and is often useful for I/O-bound tasks. Multiprocessing uses separate processes and can run CPU-bound work in parallel, at the cost of more process and data-transfer overhead.

### 45. What is the difference between a module and a package?
A module is a Python file that can be imported. A package organizes modules under a package namespace, commonly using directories and package metadata such as `__init__.py`.

## Short coding questions

### 46. How do you reverse a string?

```python
text = "python"
reversed_text = text[::-1]
```

### 47. How do you remove duplicates from a list while preserving order?

```python
values = [3, 1, 3, 2, 1]
unique_values = list(dict.fromkeys(values))
```

### 48. How do you count item occurrences?

```python
from collections import Counter

counts = Counter(["a", "b", "a"])
```

### 49. How do you safely access an optional dictionary key?

```python
name = user.get("name", "Unknown")
```

### 50. How do you check whether a value is a list?

```python
if isinstance(value, list):
    print("It is a list")
```

## How to answer interview questions well

For each concept:
1. Give a clear definition.
2. Mention when it is useful.
3. Show a short example if relevant.
4. State important tradeoffs or edge cases.

Keep answers precise. If a question involves code, explain both what it does and why the chosen approach is appropriate.
