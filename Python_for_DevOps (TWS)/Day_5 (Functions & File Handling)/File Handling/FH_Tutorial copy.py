"""
open()       the "Credentials.txt" file
operation on the "Credentials.txt" file
close()      the "Credentials.txt" file
"""

try:
    file_obj = open("Credentials.txt",'r')
    file_obj.read()
except:
    file_obj = open("Credentials.txt",'w')     
    file_obj.write("Username = SOUMOJIT\n Password = SDAS1406")
finally:
    file_obj.close()    