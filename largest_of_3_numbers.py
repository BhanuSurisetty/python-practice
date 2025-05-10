# Find the largest of 3 numbers
num1= int(input("Enter first number: " ))
num2= int(input("Enter second number: " ))
num3= int(input("Enter third number: " ))

if(num1==num2 and num1==num3):      
    print("All numbers are equal")
elif(num1==num2):                           
    print("Num 1 and Num 2 are equal")
elif(num1==num3):
    print("Num 1 and Num 3 are equal")
elif(num2==num3):
    print("Num 2 and Num 3 are equal")
elif(num1>num2 and num1>num3):
    print("Num 1 is the largest number")
elif(num2>num1 and num2 >num3):
    print("num 2 is the largest number")
else:
    print("Num 3 is the largest number")