sub1 = float(input("Enter Subject 1 marks: "))
sub2 = float(input("Enter Subject 2 marks: "))
sub3 = float(input("Enter Subject 3 marks: "))

weighted_avg = (sub1 * 0.40) + (sub2 * 0.30) + (sub3 * 0.30)

if weighted_avg >= 85:
    grade = 'A'
elif weighted_avg >= 70:
    grade = 'B'
elif weighted_avg >= 50:
    grade = 'C'
else:
    grade = 'F'

print(f"\nWeighted Average: {weighted_avg:.2f}")
print(f"Grade: {grade}")
