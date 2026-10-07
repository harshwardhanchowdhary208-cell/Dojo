# Question: Solve the input-processing challenge implemented in this program.
# Add your solution here.

while True:
    text = input("Enter the Character: ")

    def char_palindrome(text):
        reversed_text = "".join(reversed(text))

        if reversed_text == text:
            print("Character is a palindrome")
            return True
        else:
            print("Character is not a palindrome")
            return False

    if not char_palindrome(text):
        break