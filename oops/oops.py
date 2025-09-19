# Write a program that divides two numbers and handles division by zero using try and except.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

divide_numbers(10, 2)
divide_numbers(10, 0)


# 2 Ask the user to input an integer. Use try-except to handle if the input is not an integer.

def get_integer_input():
    try:
        user_input = int(input("Please enter an integer: "))
        print("You entered:", user_input)
    except ValueError:
        print("Error: That is not a valid integer.")
    finally:
        print("Execution completed.")
get_integer_input()

# 3 Open a file using open() and use try-except to catch FileNotFoundError.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

read_file("non_existent_file.txt")

# 4 Write a program that adds two numbers. Catch TypeError if the user inputs strings.
def add_numbers(num1, num2):
    try:
        result = num1 + num2
        print("Result:", result)
    except TypeError:
        print("Error: Invalid input types.")
add_numbers(5, 10)
add_numbers("5", 10)

