"""Prompts for 2 numbers to sum and prints result"""

print("Enter two numbers to sum. Enter 'q' to quit.") 

#while True is True loop the exception block (infinite loop).
while True:
    #Exception in case user fails to enter a number
    try:
        num1 = input("Enter the 1st number: ")
        if num1 == 'q':
            break
        num1 = int(num1)

        num2 = input("Enter the 2nd number: ")
        if num2 == 'q':
            break
        num2 = int(num2)
        
    except:
        print("Error: Please enter a number.")
    #Prints sum of two numbers if 2 numbers were entered.
    else:
        numsum = num1 + num2
        print("The sum of", str(num1), "and", str(num2), "is", str(numsum) + ".")


