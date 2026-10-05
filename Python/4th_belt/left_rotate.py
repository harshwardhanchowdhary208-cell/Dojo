# Question: What problem does this code solve?
# Add your solution here.

from typing import List

def left_rotate(arr: List[int], d: int) -> None:
    n = len(arr)
    if n == 0:
        return
    d = d % n
    
    # Helper function to reverse a segment in-place using pointers
    def reverse_segment(start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # 1. Reverse the first 'd' elements
    reverse_segment(0, d - 1)
    # 2. Reverse the remaining 'n - d' elements
    reverse_segment(d, n - 1)
    # 3. Reverse the entire array
    reverse_segment(0, n - 1)
