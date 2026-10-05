s = input().strip()
p = input().strip()

if s[:len(p)] == p:
    print("Yes")
else:
    print("No")
