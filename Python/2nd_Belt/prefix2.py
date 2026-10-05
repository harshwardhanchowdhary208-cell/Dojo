# Question: What problem does this code solve?
# Add your solution here.

s = input().strip()
p = input().strip()

# Check if s starts with the prefix p
if s.startswith(p):
    print("Yes")
else:
    print("No")
