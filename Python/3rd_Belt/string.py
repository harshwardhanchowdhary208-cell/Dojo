# Question: Process the input string according to the required string operation.
# Add your solution here.

s = input()
result = []

for i in range(len(s)):
    if i > 0 and s[i].isupper() and s[i-1].islower():
        result.append(" ")
    result.append(s[i])

print("".join(result))



