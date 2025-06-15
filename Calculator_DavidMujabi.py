import math
import os

os.system("clear")

global choice
def choices():
    print("Which operation do you want to perform?\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Quotient")
    print("5. Remainder")
    print("6. Power")
    print("7. Square Root")
    print("8. Convert to percentage")
    print("9. Exit")

    inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    choice  = input("\nSelect one of the above choices: ")
    if choice == "exit" or "q" or "quit" or "9":
        print("Exiting the calculator..")
        print("Thank you for using the calculator!! goodbye")
        exit()
    if not choice.strip() or choice not in inputs:
        print("\nInvalid choice please enter a valid choice!!!\n")
        choices()
    return choice
def user_input():
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))

    if not a.strip() or not b.strip():
        print("Error!!Invalid input. Please enter a valid number.")
    else:
        a = float(a)
        b = float(b)
        return a, b
def user_continue():
    print("Continue with calculation? (y/n)")
    cont = input()
    if cont.lower() == 'n' or cont.lower() == 'no' or cont.lower() == 'exit':
        print("Exiting the calculator. Thank you for using..")
        print("Maths is easy")
        exit()
    else:
        return True
    
def calculator() :
    choice = choices()
    a, b = user_input()
    if choice == "1":
        result = a + b
        print("The result is: ", result)
    elif choice == "2":
        result = a - b
        print("The result is: ", result)
    elif choice == "3":
        result = a * b
        print("The product is: ", result)
    elif choice == "4":
        if b == 0:
            print("Error!! Division by zero is not allowed.")
        else:
            result = a / b
            print("The quotient is: ", result)
    elif choice == "5":
        result = a % b
        print("The remainder is: ", result)
    elif choice == "6":
        result = pow(a, b)
        print(f"{a} to the power of {b} is: ", result)
    elif choice == "7":
        a = float(input("\nEnter the value whose square root is needed: "))
        result = math.sqrt(a)
        print(f"The square root of {a} is: ", result)
    elif choice == "8":
        a = float(input("\nEnter the value to be convereted to percentage: "))
        result = a * 100
        print(f"{a} is {result} percent")
    
def main():
    print("Calculators make better mathematicians..")
    print("Welcome to your favourite calculator\n")
    calculator()
    cont = user_continue()
    while cont:
        calculator()
main()