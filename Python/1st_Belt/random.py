x = int(input())
i = 0
while i < x and x%2==0:
    i += 1
    print(i, end=" ")
    i//2=2

x = int(input())
i = 2

while i <= x:
    print(i, end=" ")
    i += 2

x = int(input())

if x % 2 == 0:
    for i in range(1, x + 1):
        print(i, end=" ")

x = int(input())
i = 0

if x % 2 == 0:
    while i < x:
        i += 1
        print(i, end=" ")
else:
    print("x is odd")