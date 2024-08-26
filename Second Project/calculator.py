# Python program for simple calculator
 
# Function to add two numbers
def add(x, y):
    return x+y
 
# Function to subtract two numbers
def subtract (x, y):
    return x-y
 
# Function to multiply two numbers
def multiply(x, y):
    return x*y
 
# Function to divide two numbers
def divide(x, y):
    if y==0:
        return "Divide by zero error"
    return x/y

# Getting opeartion choice from th user 
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
 
 
# Take input from the user
operation = int(input("Select operations form 1, 2, 3, 4 :"))
 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#performing the entered operation 
if operation == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))
 
elif operation == 2:
    print(num1, "-", num2, "=",
                    subtract(num1, num2))
 
elif operation == 3:
    print(num1, "*", num2, "=",
                    multiply(num1, num2))
 
elif operation == 4:
    print(num1, "/", num2, "=",
                    divide(num1, num2))
else:
    print("Invalid input")

