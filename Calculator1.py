A = int(input("Enter 1st Number:"))
print(A)
B = int(input("Enter 2nd Number:"))
print(B)
C = str(input("Operation:"))
print(C)

if   C == "ADD":
    print("Result: ", A+B)
elif C == "SUB":
    print("Result: ", A-B)
elif C == "MUL":
    print("Result: ", A*B)
else:
    print("Result: ", A/B)
