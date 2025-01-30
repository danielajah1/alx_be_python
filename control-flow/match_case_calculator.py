num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

        
# Prompt the user for the operation
operators = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operators:
        case "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divid by zero")
            else:
                result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        case _:
            print("Invalid operation. Please choose one of +, -, *, or /.")
