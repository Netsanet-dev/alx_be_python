def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            try:
                return num1/num2
            except ZeroDivisionError:
                print(f"The denominator must be greater than zero")
        case _:
            print("Please enter the correct number")
    
