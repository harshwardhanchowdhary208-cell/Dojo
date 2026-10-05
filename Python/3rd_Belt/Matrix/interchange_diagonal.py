import sys

def main():
    # Read all input lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    # Parse the size of the square matrix
    n = int(input_data[0].strip())
    
    # Construct the matrix
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, input_data[i].split()))
        matrix.append(row)
        
    # Interchange the main diagonal and anti-diagonal elements
    for i in range(n):
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]
        
    # Print the modified matrix
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
