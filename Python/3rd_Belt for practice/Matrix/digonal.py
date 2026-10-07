# Question: Find the trace of a square matrix by summing its main diagonal elements.
# Add your solution here.

def trace_of_matrix(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(trace_of_matrix(matrix))