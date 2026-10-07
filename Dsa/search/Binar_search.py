def binary_search(arr, target):
    """
    Performs Iterative Binary Search on a sorted list.
    Returns the index if found, else returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Prevents potential overflow in lower-level languages
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1


# Example Usage:
sorted_arr = [5, 10, 15, 20, 25, 30, 35]
target = 30
result = binary_search(sorted_arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")