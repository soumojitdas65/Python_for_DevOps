"""
PROGRAM-ID      :   Assignment_1(Conditionals).py
PROGRAM AUTHOR  :   Soumojit Das (https://github.com/soumojitdas65)
PROGRAM DESC.   :   This Program is designed to take "INT" Inputs from User and append to a list.
                        Using the same list, we have to find the smallest & 2nd smallest Number.
PROGRAM CREATED :   August, 2022.
"""

# The List ("num_list") which will store the "INT" input variables from User.
num_list = []

# To accept the "INT" Input from User for length of the List ("num_list").
while True:
    try:
        elements = int(input("Enter the length of the list: "))
        break
    except ValueError as e1:
        print("You have enterd a non-numerical Input. Please Try Again! \n")
        continue

# To accept "INT" Inputs from User and append to a List ("num_list").
for i in range(0,elements):

    while True:
        try:
            numx = int(input("Enter Number: "))

            num_list.append(numx)
            break
        except ValueError as e:
            print("You have enterd a non-numerical Input. Please Enter Again! \n")
            continue

# To display the inputs enterd in the List ("num_list").
print("\n Your Inputs are:", num_list)

# To display the inputs enterd in the List ("num_list") in an Ascending Order.
num_list.sort()
print("\n Your Inputs sorted in Ascending Order are:", num_list)
print("\n")                                                                          # To print a new line.

# To display the Smallest & 2nd Smallest Integer Inputs from the List ("num_list") given by User.
print("     The Smallest Integer provided by User is: ", num_list[0])
print("     The Secondd Smallest Integer provided by User is: ", num_list[1])
print("\n")                                                                          # To print a new line.
