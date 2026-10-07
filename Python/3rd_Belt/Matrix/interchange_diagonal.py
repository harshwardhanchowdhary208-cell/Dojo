def interchange_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        # Swap the main diagonal element with the anti-diagonal element
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Step 1: Get the dimensions of the square matrix
n = int(input("Enter the size of the square matrix (N x N): "))

matrix = []
print(f"Enter the elements row by row (space-separated integers):")

# Step 2: Dynamically take matrix input row by row
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    # Validate if the user entered exactly N elements per row
    while len(row) != n:
        print(f"Invalid input! Please enter exactly {n} elements.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

print("\nOriginal Matrix:")
print_matrix(matrix)

# Step 3: Swap the diagonals
interchange_diagonals(matrix)

print("\nMatrix after interchanging diagonals:")
print_matrix(matrix)
