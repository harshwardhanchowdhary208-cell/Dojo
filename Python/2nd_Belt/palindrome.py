# Question: What problem does this code solve?
# Add your solution here.

x=input('Enter the number:')
char=x.lower()
if str(char) == str(char)[::-1]:
    print('Number is a palindrome') 
else:
    print('number is not a palindrome')