# Question: What problem does this code solve?
# Add your solution here.

def print_reversed_matrix(rows, cols, matrix):
    for row in matrix[::-1]:
        print(" ".join(map(str, row)))

def main():
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    
    print_reversed_matrix(rows, cols, matrix)

if __name__ == "__main__":
    main()
