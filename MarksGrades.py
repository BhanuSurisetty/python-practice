# Take user input of a mark (0–100) and print grade (A/B/C/Fail)
marks = int(input("Enter your marks: "))
if marks>=80:
    print("Grade A")
elif marks>=60:
    print("Grade B")
elif marks>=35:
    print("Grade C")
else:
    print("Fail")

