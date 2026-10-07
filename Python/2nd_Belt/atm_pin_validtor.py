# Question: Check whether the entered ATM PIN is valid.
# Add your solution here.

correct_pin = "4321"
attempts = 0
max_attempts = 3
access_granted = False

print("Welcome to the ATM PIN Validator!")

while attempts < max_attempts:
    pin_entered = input(f"Enter your PIN (Attempt {attempts + 1}/{max_attempts}): ")
    attempts += 1

    if pin_entered == correct_pin:
        access_granted = True
        print(f"Access Granted! You used {attempts} attempt(s).")
        break
    else:
        print("Incorrect PIN.")

if not access_granted:
    print(f"Access Denied. You have used all {max_attempts} attempts.")
