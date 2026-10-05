# Question: What problem does this code solve?
# Add your solution here.

def is_sparse(matrix, M, N):
    zero_count = sum(row.count(0) for row in matrix)
    
    total_elements = M * N
    
    return zero_count >= (total_elements / 2)
