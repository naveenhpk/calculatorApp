import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to calculate percentage
def percentage(x, y):
    return (x * y) / 100

# Function to calculate exponentiation
def power(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    return math.sqrt(x)

# Function to calculate factorial
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

# Function to display the menu and get user choice
def display_menu():
    print("Advanced Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Exit")
    choice = input("Enter your choice (1-9): ")
    return choice

# Main program
while True:
    choice = display_menu()

    if choice == '9':
        print("Exiting the calculator.")
        break

    num1 = float(input("Enter first number: "))

    if choice not in ['7', '8', '9']:  # For operations requiring two numbers
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        percentage_value = float(input("Enter percentage value: "))
        print("Result:", percentage(num1, percentage_value))
    elif choice == '6':
        print("Result:", power(num1, num2))
    elif choice == '7':
        print("Result:", square_root(num1))
    elif choice == '8':
        if num1 < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Result:", factorial(int(num1)))
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
