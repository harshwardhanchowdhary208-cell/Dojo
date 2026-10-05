# Question: What problem does this code solve?
# Add your solution here.

from typing import List

def move_zeroes(arr: List[int]) -> None:
    write_index = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            # Swap the non-zero element with the element at write_index
            arr[i], arr[write_index] = arr[write_index], arr[i]
            write_index += 1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    move_zeroes(arr)
    print(" ".join(map(str, arr)))
