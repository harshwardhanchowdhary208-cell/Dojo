# Question: What problem does this code solve?
# Add your solution here.

def is_magic_square(matrix, N):
    target_sum = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != target_sum:
            return False
            
    for col in range(N):
        col_sum = sum(matrix[row][col] for row in range(N))
        if col_sum != target_sum:
            return False
            
    diag1_sum = sum(matrix[i][i] for i in range(N))
    if diag1_sum != target_sum:
        return False
        
    diag2_sum = sum(matrix[i][N - 1 - i] for i in range(N))
    if diag2_sum != target_sum:
        return False
        
    return True

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(is_magic_square(matrix, N))
