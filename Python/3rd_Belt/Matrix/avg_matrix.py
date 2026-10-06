# Question: What problem does this code solve?
# Compute the average value of all elements in a matrix.


def average_of_matrix(matrix):
    if not matrix or not matrix[0]:
        return 0.0

    total_sum = sum(sum(row) for row in matrix)
    total_elements = sum(len(row) for row in matrix)
    return total_sum / total_elements


if __name__ == "__main__":
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    print(f"{average_of_matrix(matrix):.1f}")
