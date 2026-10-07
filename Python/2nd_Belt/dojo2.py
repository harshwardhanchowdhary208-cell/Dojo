# Question: Solve the given Dojo challenge using the specified logic.
# Add your solution here.

def sum_digits_until_single(num):

    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        num = total
    return num

user_input = input("Enter a non-negative integer: ").strip()

if not user_input.isdigit():
    raise ValueError("Input must be a non-negative integer.")

number = int(user_input)

result = sum_digits_until_single(number)
print(f"Single-digit sum: {result}")
