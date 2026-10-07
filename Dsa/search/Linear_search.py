def linear_search(arr, target):
    """
    Performs Linear Search to find the target in the list.
    Returns the index if found, else returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example Usage:
arr = [10, 25, 7, 42, 18]
target = 42
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")