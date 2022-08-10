# This is an updated version of Calculator which was originally written by Soham Gupta (https://www.linkedin.com/in/soham-gupta-in/) 
# To access the original code from Soham, Please go to https://github.com/gupta-soham/Calculator-in-Python/blob/main/calculator.py

print("Welcome to CalculatorThree_v3.0\n Please choose from the valid Operators shown below:")
print("1. Addtion (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponent (**)")
print("6. Remainder (%)")


while True:
# User provides the 2nd Number as Input (Integer or Float)
    option = input("Enter your requested Operator:\n")                  # Lets User enter a valid Operator from above-mentioned list.

    if option in ("1", "2", "3", "4", "5", "6"):
        n1 = float(input("Enter your 1st Number: "))                                   # User provides the 1st Number as Input (Integer or Float)
        n2 = float(input("Enter your 2nd Number: "))  
    
    
        if option == "1":
            print(n1, "+", n2,"=", n1+n2)
            
        elif option == "2":
            print(n1, "-", n2,"=", n1-n2)
            
        elif option == "3":
            print(n1, "*", n2,"=", n1*n2)
            
        elif option == "4":
            print(n1, "/", n2,"=", n1/n2)
            
        elif option == "5":
            print(n1, "^", n2,"=", n1**n2)
            
        elif option == "6":
            print(n1, "//", n2,"=", n1%n2)
       

# This part of code lets User decide if the person wants to end the Calculator or still continue....                  
        print("Do you want to Continue ? (Y/N)")
        response = str(input(("Your Response: ")))

        if response == "N":
            break
    else:
        print("Invalid Option for Operator")
