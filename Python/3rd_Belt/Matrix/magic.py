# Question: Check whether a square matrix is a magic square.
# Add your solution here.


def is_magic_square(matrix, N=None):
    if not matrix or not matrix[0]:
        return False

    n = len(matrix) if N is None else N
    if n <= 0:
        return False

    target_sum = sum(matrix[0])

    for row in matrix:
        if len(row) != n or sum(row) != target_sum:
            return False

    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False

    diag1_sum = sum(matrix[i][i] for i in range(n))
    if diag1_sum != target_sum:
        return False

    diag2_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2_sum != target_sum:
        return False

    return True


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(is_magic_square(matrix))
