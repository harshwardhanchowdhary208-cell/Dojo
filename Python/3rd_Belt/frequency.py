# Question: Count how many times each character appears in a string.
# Add your solution here.

str = input()
str = str.lower()
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)