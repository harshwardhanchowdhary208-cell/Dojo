# Question: Add two matrices of equal size.
# Add your solution here.


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


if __name__ == "__main__":
    rows, cols = map(int, input().split())
    matrix1 = [list(map(int, input().split())) for _ in range(rows)]

    rows2, cols2 = map(int, input().split())
    matrix2 = [list(map(int, input().split())) for _ in range(rows2)]

    result = add_matrices(matrix1, matrix2)
    for row in result:
        print(*row)