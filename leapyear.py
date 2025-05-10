# Check if a given year is a leap year
num = int(input("enter a year: "))
if(num %4==0 and num%100!=0  or num%400==0):
    print(num, "is a leap year")
else:
    print(num, "is not a leap year")