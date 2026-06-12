num1 = int(input("number 1:"))
num2 = int(input("number 2:"))

def add(num1, num2):
    return (num1+num2)
print(num1, "+", num2, "=", add(num1,num2))

def subtract(num1, num2):
    return (num1-num2)
print(num1, "-", num2, "=", subtract(num1,num2))

def multiply(num1, num2):
    return (num1*num2)
print(num1, "*", num2, "=", multiply(num1,num2))

def divide(num1, num2):
    return (num1/num2)
print(num1, "/", num2, "=", divide(num1,num2))