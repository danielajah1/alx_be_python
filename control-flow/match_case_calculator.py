# Prompt user for the numbers
num1 = input ("Enter the first number: ")
num2 = input ("Enter the second number: ")

# Prompt user for operators.
choose_operator = input ("Choose the operation (+, -, *, /): ")

# Prompt the user for input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

        # Prompt the user for the operation
match choose_operator:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
            print("Invalid operation. Please choose one of +, -, *, or /.")