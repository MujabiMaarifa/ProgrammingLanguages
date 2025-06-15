import math
import os
os.system("clear")

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
def root(a):
    return math.sqrt(a)

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
        result = root(a)
        print(f"\nSquare root displays: {result:.4f}")
    else:
        print("Invalid operator")
    
# user inputs
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %, ^): ")
calculator()

# prompt user to continue
proceed = input("\nDo you want to continue with another calculation? (Y/n/exit): ")
while proceed.lower() == "y":
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %, ^): ")
    calculator()
    proceed = input("\nDo you want to continue with another calculation? (Y/n): ")
else:
    print("\nThank you for using the calculator. Goodbye!")
