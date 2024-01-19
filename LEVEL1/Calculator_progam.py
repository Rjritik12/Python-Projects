def calculate(operation, num1, num2):
    
    operation = int(operation)
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        else:
            return num1 / num2
    elif operation == 5:
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        else:
            return num1 % num2
    else:
        return "Invalid operation"

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    user_choice = input("Enter choice (1/2/3/4/5): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = calculate(user_choice, num1, num2)
    print(result)