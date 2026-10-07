# Question: Print Pascal's triangle for the given number of rows.
# Add your solution here.

import math

def print_pascal_math(n):
    for i in range(n):
        print(" " * (n - i), end="")
        
        for j in range(i + 1):
            print(math.comb(i, j), end=" ")
            print()

print_pascal_math(5)
