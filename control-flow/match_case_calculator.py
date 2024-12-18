# Prompt the user the enter a number and choose operations
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))

# Performing calculations
match operation:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * numebr2)
    case "/":
        try:
           print(number1 / number2)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
