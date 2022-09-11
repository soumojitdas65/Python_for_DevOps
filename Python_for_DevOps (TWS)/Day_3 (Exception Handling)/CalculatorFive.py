# This version of Calculator is based upon Conditions, Loops and Exception Handling.

print("Welcome to Calculator_v5.0\n Please choose from the valid Operators shown below:")
print("1. Addtion (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponent (**)")
print("6. Remainder (%)")


while True:
    n1 = input("Enter your 1st Number: ")                                   # User provides the 1st Number as Input (Integer or Float)
    n2 = input("Enter your 2nd Number: ")                                   # User provides the 2nd Number as Input (Integer or Float)
    option = int(input("Enter your requested Operator: "))                  # Lets User enter a valid Operator from above-mentioned list.

    if option not in ("1", "2", "3", "4", "5", "6"):
        print("Invalid Option for Operator")
    else:
        if      option == "1":
                    print(n1, "+", n2,"=", n1+n2)
        elif    option == "2":
                    print(n1, "-", n2,"=", n1-n2)
        elif    option == "3":
                    print(n1, "*", n2,"=", n1*n2)
        elif    option == "4":
                    print(n1, "/", n2,"=", n1/n2)
        elif    option == "5":
                    print(n1, "^", n2,"=", n1**n2)
        elif    option == "6":
                    print(n1, "//", n2,"=", n1%n2)

