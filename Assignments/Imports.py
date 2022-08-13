"""
PROGRAM-ID      :   Assignment_2(Imports).py
PROGRAM AUTHOR  :   Soumojit Das (https://github.com/soumojitdas65)
PROGRAM DESC.   :   This Program is designed to convert a Dictionary into JSON.
PROGRAM CREATED :   August, 2022.
"""
# To import JSON Library.
import json

# The Dictionary (my_dict) which will store the Inputs from User.
my_dict = {"Name":[],"City":[],"Age":[]}

# To accept "INT" values as length of Dictionary (my_dict).
while True:
    try:
        elements = int(input("Enter the Pair(Number) of details in you want to add: "))
        break
    except ValueError as e1:
        print("You have enterd a non-numerical Input. Please Try Again! \n")
        continue

# To accept values from User to enter in the Dictionary (my_dict).
for i in range(0,elements):
    try:
        name1 = str(input("Enter your Name: ")).upper()
        city1 = str(input("Enter your City Location: ")).upper()
        agex  = int(input("Enter you Age: "))
        age1  = abs(agex)                                               # To convert -ve integers to +ve integers.
            
        my_dict["Name"].append(name1) 
        my_dict["City"].append(city1) 
        my_dict["Age"].append(age1)  
    except ValueError as e2:
        print("You entered incorrect data. Simulator is Closing !")
        i = i+1                                                         # To be used for program to only display Correct Values.
        break

if i < 1:
# To display the Dictionary created from the Inputs provided by the User.
    print("\n   The Dictionary created by the User in Python: ", my_dict)

# To display the Dictionary created from the Inputs provided by the User in JSON Format.
    json_my_dict = json.dumps(my_dict, indent = 7)
    print("\n   The Dictionary created by the User in JSON: ", json_my_dict)
