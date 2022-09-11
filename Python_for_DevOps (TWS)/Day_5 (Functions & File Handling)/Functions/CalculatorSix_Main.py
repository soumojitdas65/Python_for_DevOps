"""
This program calls another program (Calculator_Functions.py) from this Program.
    For ME:    This is like Main Program (CBL) which calls the Process Copybook (CBLCPY).
"""

from CalculatorSix_Functions import sum_nums, diff_nums, prod_nums, div_nums, exp_nums, rem_nums

print("Welcome to CalculatorThree_v6.0\n Please choose from the valid Operators shown below:")
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
        
        if option == "1":
            sum_nums()
            
        elif option == "2":
            diff_nums()
            
        elif option == "3":
            prod_nums()
            
        elif option == "4":
            div_nums()
            
        elif option == "5":
            exp_nums()
            
        elif option == "6":
            rem_nums()

# This part of code lets User decide if the person wants to end the Calculator or still continue....                  
        print("Do you want to Continue ? (Y/N)")
        response = str(input(("Your Response: ")))

        try:
            if response.upper() == "N":
                print("Calculator is Closing... Goodbye !!!")
                break
            if response.upper() == "Y":
                print("Let's start from the beginning... Shall We ?")
                continue
        except ValueError:
                print("Invalid Option for Operator !!! Let's try again...")
                continue