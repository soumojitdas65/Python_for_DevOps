# Exception Handling Tutorial.

cloud_env = ["AWS", "GCP", "AZURE"]

print("0. AWS")
print("1. GCP")
print("2. AZURE")

while True:
        i = int(input("Please select an Environment: "))

        try:
            print(cloud_env[i])
        except IndexError as x:
            print(x,"/Incorrect Value Selected. Please try again !")
            continue
        finally:
            choose = str(input("Do you wanna try again ? (Y/N): "))
# This part needs to be corrected so that it only accepts "str" input. If Numerical ("int"/ "float") is given, it should throw error
#       and go back to user entering "CHOOSE" value.
            try:
                if      choose.upper() == "Y":
                        continue
                elif    choose.upper() == "N":
                        print("Simulator is closing, Goodbye !")
                        break
#                else:
                        print("Entered value is not 'Y' or 'N'. Simulator is closing, Goodbye !")
                        break
# I think ValueError is not the correct error to check if Value entered is "str" or "int/float".
            except Exception as e:
#                print("Incorrect Response Given! Please wait while the Simulator is restarting...")
                print(e)
                continue               