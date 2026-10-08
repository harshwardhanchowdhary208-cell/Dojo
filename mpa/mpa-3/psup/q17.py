n = int(input())
amounts = []
for _ in range(n):
    amounts.append(int(input()))

budget = 0
standard = 0
premium = 0
qualified = []
adjusted = []

for amt in amounts:
    # Band classification
    if amt < 500:
        budget += 1
    elif amt <= 1999:
        standard += 1
    else:
        premium += 1

    # Qualification check
    if 1000 <= amt <= 3000:
        qualified.append(amt)
        adjusted.append(amt - 100)

print(f"Budget: {budget}")
print(f"Standard: {standard}")
print(f"Premium: {premium}")
print(f"Qualified: {qualified}")
print(f"Adjusted: {adjusted}")