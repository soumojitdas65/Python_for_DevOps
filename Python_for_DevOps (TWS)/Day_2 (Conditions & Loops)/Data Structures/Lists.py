## List Basic Code.


# print(dir(names))
names = list()

names.append("Shubham")
names.append("Soumojit")
names.append("Sudipto")
names.append("Soham")
names.append("Himanshu")

print(names)
print(names[1])

# print 5 Cloud Environments

cloud_env = ["Azure", "AWS", "GCP", "IBM"]

for i in cloud_env:
    print(cloud_env)

    if      i == "Azure":
        print("Azure")
    elif    i == "AWS":
        print("AWS")
    elif    i == "GCP":
        print("GCP")
    elif    i == "IBM":
        print("IBM")
    else:
        print("Invalid")
