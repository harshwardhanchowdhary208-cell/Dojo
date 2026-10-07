# Question: Read an n x m matrix and print it exactly as it is entered.
# Add your solution here.

# Read the number of rows (n) and columns (m)
n, m = map(int, input().split())

# Read each row of the matrix
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Print the matrix row by row, with elements separated by a space
for row in matrix:
    print(*row)
