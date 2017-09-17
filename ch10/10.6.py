"""Prompts for 2 numbers to sum and prints result"""

print("Enter two numbers to sum.") 

#Exception in case user fails to enter a number
try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
except:
    print("Error: Please enter a number.")
#Prints sum of two numbers if 2 numbers were entered.
else:
    numsum = num1 + num2
    print("The sum of", str(num1), "and", str(num2), "is", str(numsum) + ".")


