"""Prompts for 2 numbers to sum and prints result"""

print("Enter two numbers to sum.") 
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

#Exception in case user fails to enter a number
try:
    num1 = int(num1)
    num2 = int(num2)
    numsum = num1 + num2

except:
    print("Error: Please enter a number.")

    while num1.isdigit() == False | num2.isdigit() == False:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        numsum = num1 + num2
        print("The sum of", str(num1), "and", str(num2), "is", str(numsum) + ".")

#Prints sum of two numbers if 2 numbers were entered.
else:
    
    print("The sum of", str(num1), "and", str(num2), "is", str(numsum) + ".")


