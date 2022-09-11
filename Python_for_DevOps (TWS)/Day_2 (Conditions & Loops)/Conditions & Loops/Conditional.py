# Condition Tutorial Basic Code.
#   "if"   condition.
#   "elif" condition.
#   "else" condition.

"""

This Script checks if 
My Cloud Environment is amongst the following
- AWS
- Azure
- GCP

"""

cloud_env       =   input("Enter Cloud Environment: ")
cloud_service   =   input("Enter Cloud Service: ")

if      cloud_env.upper == "AWS":
    print("You are in AWS")
    if  cloud_service.upper == "EC2":
        print("You are using EC2 in AWS")
    else:
        print("But not using AWS Service")
elif    cloud_env.upper == "Azure":
    print("You are in Azure")
    if  cloud_service.upper == "VM":
        print("You are using VM in Azure")
    else:
        print("But not using Azure Service")
elif    cloud_env.upper == "GCP":
    print("You are in GCP")
    if  cloud_service.upper == "GBUILD":
        print("You are using GBuild in Azure")
    else:
        print("But not using GCP Service")
else:
    print("Incorrect Environment or Service")
