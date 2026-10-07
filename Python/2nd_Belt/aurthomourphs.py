# Question: Check whether the given strings are anagrams.
# Add your solution here.

def is_automorphic(n):
    square = n ** 2
    
    return str(square).endswith(str(n))

n = int(input())

if is_automorphic(n):
    print("true")
else:
    print("false")
