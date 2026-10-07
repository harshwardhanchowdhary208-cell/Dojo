# Question: Compute the prefix sum of each element in the array.
# Add your solution here.

s = input().strip()
p = input().strip()

if s[:len(p)] == p:
    print("Yes")
else:
    print("No")
