# Question: What problem does this code solve?
# Add your solution here.

text=input()
vowels=0
consonants=0
for char in text:
        if char.lower() in "aeiou":
            vowels+=1
        elif char.lower() in "qwrtysdfghjklzxcvbnmp":
            consonants+=1
print(vowels)
print(consonants)