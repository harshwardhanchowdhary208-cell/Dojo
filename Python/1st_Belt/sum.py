# Question: Calculate the sum of the given numbers.
# Add your solution here.

num=int(input("Enter a non-negative integer: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(total)