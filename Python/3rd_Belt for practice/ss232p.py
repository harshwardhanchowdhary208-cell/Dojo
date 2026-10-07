# Question: Solve the given array/string challenge using the required logic.
# Add your solution here.

a=input()
b=input()
c = False
for i in a:
    if a[i:len(b)]==b:
        print(a[:i]+a[i+len(b):])
        c=True
        break
if not c:
    print(a)