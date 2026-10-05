# Question: What problem does this code solve?
# Add your solution here.

word = input()
words = word.split()
longest = max(words, key=len)
print(longest)
