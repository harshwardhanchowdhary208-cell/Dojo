word = input()
words = word.split()
longest = max(words, key=len)
print(longest)
