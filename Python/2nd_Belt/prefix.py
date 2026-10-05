# Question: What problem does this code solve?
# Add your solution here.

s = input().strip()
p = input().strip()

if s[:len(p)] == p:
    print("Yes")
else:
    print("No")
