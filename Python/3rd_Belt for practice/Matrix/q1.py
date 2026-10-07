# Question: Add two matrices of equal size.
# Add your solution here.

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
matrix1 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows)]
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
matrix2 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(rows)]

def add_matrices(matrix1, matrix2):

    rows = len(matrix1)
    cols = len(matrix1[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]    
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

print(add_matrices(matrix1, matrix2))