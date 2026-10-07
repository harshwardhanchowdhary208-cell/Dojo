# Question:
# Given an integer N, print the first N odd numbers separated by spaces.
# Example: Input: 5 -> Output: 1 3 5 7 9

n = int(input())
for i in range(1, 2 * n, 2):
    print(i, end=" ")
print()
