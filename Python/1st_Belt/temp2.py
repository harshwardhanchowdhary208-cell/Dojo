# Question: What problem does this code solve?
# Add your solution here.

temp = float(input("Enter the temperature value: "))

unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {fahrenheit:.2f}°F")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid unit entered. Please enter 'C' or 'F'.")