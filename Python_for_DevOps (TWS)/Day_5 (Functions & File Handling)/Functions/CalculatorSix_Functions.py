"""
This code is a tutorial for Defining a "Function" & calling the same.
    For ME:     You can think of this like a Porcess Copybook (CBL/ CBLCPY) for the Main Program to call and execute.
"""

def sum_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a + b
    print("Sum of the inputs are: ", c)

def diff_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a - b
    print("Sum of the inputs are: ", c)

def prod_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a * b
    print("Sum of the inputs are: ", c)

def div_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a / b
    print("Sum of the inputs are: ", c)

def exp_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a ** b
    print("Power Value is: ", c)

def rem_nums():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    c =  a // b
    print("Remainder is ", c)