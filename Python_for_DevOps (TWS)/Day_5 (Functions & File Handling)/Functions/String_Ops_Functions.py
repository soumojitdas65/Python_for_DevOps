"""
This code is a tutorial for Defining a "Function" & calling the same.
    For ME:     You can think of this like a Porcess Copybook (CBL/ CBLCPY) for the Main Program to call and execute.
"""

def string_case():
    word = input("Enter your word: ")

    if word.islower():
        print("Input in lower case: ", word)
    elif word.isupper():
        print("Input in UPPER case: ", word)
    else:
        print("Input given by user: ", word)