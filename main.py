def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def user_input():
    """Function to get user input."""
    
    operation = input("Choose operation +, -, /, * : ")
    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")
    
    return (operation, num_1, num_2)

def main():
    operation, num_1, num_2 = user_input()
    if operation == "+":
        answer = addition(num_1, num_2)
    elif operation == "-":
        answer = subtraction(num_1, num_2)
    elif operation == "*":
        answer = multiplication(num_1, num_2)
    elif operation == "/":  
        answer = division(num_1, num_2)

    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()
    