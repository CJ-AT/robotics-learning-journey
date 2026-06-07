def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sign = input("Enter operation (+, -, *, /): ")

if sign == "+":
    print("Addition:", add(a,b))
elif sign == "-":
    print("Subtraction:", subtract(a,b))
elif sign == "*":
    print("Multiplication:", multiply(a,b))
elif sign == "/":
    print("Division:", divide(a,b))