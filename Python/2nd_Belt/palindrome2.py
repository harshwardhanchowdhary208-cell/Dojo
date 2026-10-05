# Question: What problem does this code solve?
# Add your solution here.

num = int(input("Enter the number:"))

def is_palindrome_math(num: int) -> bool:

    if num < 0 or (num % 10 == 0 and num != 0):
        reversed_num=0
        m=num
        n=reversed_num

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    if n == m:
        print(f"The number {num} is a palindrome.")
    else:
        print(f"The number {num} is not a palindrome.")

