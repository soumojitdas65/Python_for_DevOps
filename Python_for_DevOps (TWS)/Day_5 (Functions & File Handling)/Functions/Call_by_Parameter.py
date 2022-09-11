# Tutorial for Call By Parameter Functions.

def check_env(list_env):
    output = []
    for env in list_env:
        if      env.upper() == "AWS":
                output.append("You are in AWS")
        elif    env.upper() == "AZURE":
                output.append("You are in Azure")
        else:
                output.append("You are in GCP")
    return output

output = check_env(["aws", "Azure"])
print(output)