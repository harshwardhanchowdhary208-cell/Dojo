# Question: Check whether the entered ATM PIN is valid.
# Add your solution here.

for i  in range(3):
 password="4321"
 user_password=input()
 if password==user_password:
    print("access is granted")
 else:
   print("access is not granted")