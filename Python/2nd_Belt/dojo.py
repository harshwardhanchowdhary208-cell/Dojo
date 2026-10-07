# Question: Solve the given Dojo challenge using the specified logic.
# Add your solution here.

def calculate_age(present_year, birth_year):
    age = present_year - birth_year
    return age
def main():
    present_year = int(input("Enter the present year: "))
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(present_year, birth_year)
    print(f"You are {age} years old.")
if __name__ == "__main__":
    main()