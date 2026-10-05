def is_lower_triangular_matrix(matrix):
    m = len(matrix)
    if m == 0:
        return True
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if i < j and matrix[i][j] != 0:
                return False
    return True

try:
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    
    print("Yes" if is_lower_triangular_matrix(matrix) else "No")
    
except ValueError:
    print("Invalid input. Please follow the input format: '<rows> <cols>' followed by the matrix rows.")
