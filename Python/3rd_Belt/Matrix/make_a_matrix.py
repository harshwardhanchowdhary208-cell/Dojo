r, c = map(int, input().split())
matrix = []
for i in range(r):
  row = list(map(int, input().split()))
  matrix.append(row)
for i in range(r):
  for j in range(c):
    print(matrix[i][j], end = " ")
  print()