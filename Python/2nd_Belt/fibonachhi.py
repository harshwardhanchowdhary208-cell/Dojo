n = input()
a, b = n[0], n[1]
for i in range(int(n)):
    print(a, end=" ")
    a, b = b, a + b
