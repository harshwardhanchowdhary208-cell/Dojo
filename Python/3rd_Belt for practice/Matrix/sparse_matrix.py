# Question: Check whether a matrix is sparse by counting how many zero elements it contains.
# Add your solution here.

def is_sparse(matrix, M, N):
    zero_count = sum(row.count(0) for row in matrix)
    
    total_elements = M * N
    
    return zero_count >= (total_elements / 2)
