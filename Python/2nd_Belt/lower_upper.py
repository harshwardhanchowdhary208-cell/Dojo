# Question: What problem does this code solve?
# Add your solution here.

s = input()

result = []

for i in range(len(s)):
    if i > 0 and s[i].isupper() and s[i-1].islower():
        result.append(" ")
    
    result.append(s[i])

print("".join(result))