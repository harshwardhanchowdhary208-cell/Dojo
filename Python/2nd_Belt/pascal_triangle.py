# Question: What problem does this code solve?
# Add your solution here.

def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        # Create a row with 1s
        row = [1] * (i + 1)
        # Calculate middle values
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    for row in triangle:
        print(" " * (n - len(row)), end="")
        print(" ".join(map(str, row)))


print_pascals_triangle(5)
