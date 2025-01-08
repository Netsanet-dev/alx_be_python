def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        try:
            return num1/num2
        except ZeroDivisionError:
                print("The denominator must be greater than zero")
    else:
        print("Please enter the correct number")
    
