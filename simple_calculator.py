# Simple calculator Arithmetic operations in Python

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: +, -, *, /, %")
op = input("Enter operator: ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)
elif op == '%':
    print("Result:", num1 % num2)
else:
    print("Invalid operator!")
