"""
open()       the "Credentials.txt" file
operation on the "Credentials.txt" file
close()      the "Credentials.txt" file
"""

file_obj = open("Credentials.txt",'r')
creds = file_obj.readlines()
file_obj.close()    

for cred in creds:
    print(cred.split("=")[1])