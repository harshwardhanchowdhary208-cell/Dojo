# Question: Find the longest word in a sentence.
# Add your solution here.

word = input()
words = word.split()
longest = max(words, key=len)
print(longest)
