num1_input = input("Enter the first number: ")
num1 = float(num1_input)
num2_input = input("Enter the second number: ")
num2 = float(num2_input) 

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is: {result}")
else:
    print("Invalid operation.")
