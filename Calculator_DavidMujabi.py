import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def product(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a % b
def power(a, b):
    return pow(a, b)
def square_root(a):
    return math.sqrt(a)
def percentage(a):
    return a *100
def continue_func():
    # prompt user to continue
    proceed = input("\nContinue with another calculation? (Y/n): ")
    while proceed.lower() == "y":
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, %, ^): ")
        calculator()
        proceed = input("\nDo you want to continue with another calculation? (Y/n): ")
    else:
        print("\nThank you for using the calculator. Goodbye!")
        exit()
#main function
def calculator():
    if operator == "+":
        result = add(a, b)
        print(f"\nAddition displays: {result:.4f}")
    elif operator == "-":
        result = subtract(a, b)
        print(f"\nSubtraction displays: {result:.4f}")
    elif operator == "*":
        result = product(a, b)
        print(f"\nMultiplication displays: {result:.4f}")
    elif operator == "/":
        result = division(a, b)
        print(f"\nDivision displays: {result:.4f}")
    elif operator == "%":
        result = modulus(a, b)
        print(f"\nModulus displays: {result:.4f}")
    elif operator == "^":
        result = power(a, b)
        print(f"\nPower displays: {result:.4f}")
    elif operator == "sqrt":
        result = square_root(a)
        print(f"\nSquare root displays: {result:.4f}")
    elif operator == "p%":
        result = percentage(a)
        print(f"\n {a} in percentage is: {result}")

# user inputs
a = (input("Enter the first number: "))
b = (input("Enter the second number: "))
#validate the two inputs
if not a.strip() or not b.strip():
    print("Error!! Neither A nor B can be empty: ")

a = float(a)   
b = float(b)
operator = ['+', '-', '*', '/', '%', '^', 'sqrt']
#operator validation
while True:
    op = input("Enter the operator: ")
    if op not in operator:
        print(f"Invalid operator {op}!! Please enter a valid operator")
        break
    else : 
        continue
calculator()
continue_func()
