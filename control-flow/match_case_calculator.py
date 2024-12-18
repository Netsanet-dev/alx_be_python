# Prompt the user the enter a number and choose operations
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))

# Performing calculations
match operation:
    case "+":
        print(f'The result is {number1 + number2}.')
    case "-":
        print(f'The result is {number1 - number2}.')
    case "*":
        print(f'The result is {number1 * number2}.')
    case "/":
        try:
           print(f'The result is {number1 / number2}.')
        except ZeroDivisionError:
            print("Cannot divide by zero.")
