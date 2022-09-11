# This is an updated version of Calculator taking more Inputs from User.

Num1 = float(input("Enter First Number: "))
Num2 = float(input("Enter Second Number: "))
Type = str(input("Data type Requested (INT or FLT): "))      # for CalculatorTwo_v2.0

# This is Calculatortwo_v1.0 (Use by removing "#") which computes the result directly into "FLOAT" values
#       print("Addition of Num1 & Num2: ", Num1+Num2)
#       print("Subtraction of Num1 & Num2: ", Num1-Num2)
#       print("Multiplication of Num1 & Num2: ", Num1*Num2)
#       print("Division of Num1 & Num2: ", Num1/Num2)
#       print("Num1 to the power of Num2: ", Num1**Num2)

# This is Calculatortwo_v2.0 (user by removing "#") which computes the result baseed on User's Requested Data Type
if Type == "FLT":
        print("Additon of Num1 & Num2: ", float(Num1 + Num2))
        print("Subtraction of Num1 & Num2: ", float(Num1 - Num2))
        print("Multiplication of Num1 & Num2: ", float(Num1 * Num2))
        print("Division of Num1 & Num2: ", float(Num1 / Num2))
        print("Num1 to the power of Num2: ", float(Num1 ** Num2))
elif Type == "INT":
        print("Additon of Num1 & Num2: ", int(Num1 + Num2))
        print("Subtraction of Num1 & Num2: ", int(Num1 - Num2))
        print("Multiplication of Num1 & Num2: ", int(Num1 * Num2))
        print("Division of Num1 & Num2: ", int(Num1 / Num2))
        print("Num1 to the power of Num2: ", int(Num1 ** Num2))
else:
        print("Incorrect 'Data Type' Requested")