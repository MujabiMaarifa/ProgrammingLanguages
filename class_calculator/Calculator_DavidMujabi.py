import math

#function that contains the valid choices provided to the user
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
    print("9. Load Calculation History")
    print("10. Exit")

    inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    choice  = input("\nSelect one of the above choices: ")
    if not choice.strip() or choice not in inputs:
        print("\nInvalid choice please enter a valid choice!!!\n")
        choices()
    if choice == '10':
        print("\nExiting the calculator!!!\n")
        exit()
    else:
        return choice
#function to handle user's input values
def user_input():
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))

    if not a.strip() or not b.strip():
        print("Error!!Invalid input. Please enter a valid number.")
    else:
        a = float(a)
        b = float(b)
        return a, b
#function for the user to continue using the calculator or exit
def user_continue():
    cont = input("Continue with calculation? (y/n): ")
    if cont.lower() == 'n' or cont.lower() == 'no' or cont.lower() == 'exit' or cont.lower() == 'quit':
        print("\nExiting the calculator. Thank you for using..")
        print("\nProgramming and Maths is easy.. Just do it !.!")
        exit()
    else:
        return True
#function to save user's calculation history
def save_calculations(operation, result):
    try:
        with open('calculations.txt', 'a') as file:
            file.write(f"Operation: {operation}\nResult: {result}\n\n")
            print("\nCalculations saved successfully.")
    except FileNotFoundError:
        print("\nError occurred while saving calculations.")
    finally:
        file.close()
#function to perform the operations based on user's input
def calculator() :
    choice = choices()
    if choice in ['1', '2', '3', '4', '5', '6']:
        a, b = user_input()  
    if choice == "1":
        result = a + b
        print("The result is: ", result)
        save_calculations(f"{a} + {b} = ", result)
    elif choice == "2":
        result = a - b
        print("The result is: ", result)
        save_calculations(f"{a} - {b} = ", result)
    elif choice == "3":
        result = a * b
        print("The product is: ", result)
        save_calculations(f"{a} * {b} = ", result)
    elif choice == "4":
        if b == 0:
            print("Error!! Division by zero is not allowed.")
        else:
            result = a / b
            print("The quotient is: ", result)
            save_calculations(f"{a} / {b} ", result)
    elif choice == "5":
        result = a % b
        print("The remainder is: ", result)
        save_calculations(f"{a} % {b} ", result)
    elif choice == "6":
        result = pow(a, b)
        print(f"{a} to the power of {b} is: ", result)
        save_calculations(f"{a} ^ {b} ", result)
    elif choice == "7":
        a = float(input("\nEnter the value whose square root is needed: "))
        result = math.sqrt(a)
        print(f"The square root of {a} is: ", result)
        save_calculations(f"{a} square root: ", result)
    elif choice == "8":
        a = float(input("\nEnter the value to be converted to percentage: "))
        result = a * 100
        print(f"{a} is {result} percent")
        save_calculations(f"{a} as percent is: ", result)
    elif choice == "9":
        print("The Calculations done are as shown below..\n")
        with open('calculations.txt', 'r') as file:
            print(file.read())
            print("\nFile read successfully\n")
    elif choice == "10":
        print("Exiting the calculator..")
        print("Thank you for using the calculator!! goodbye")
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")
# main function that runs the calculator
if __name__ == "__main__": #only execute the main function when it is called
    def main():
        print("Calculators make better mathematicians..")
        print("Welcome to your favourite calculator\n")
        calculator()
        cont = user_continue()
        while cont:
            calculator()
    main()