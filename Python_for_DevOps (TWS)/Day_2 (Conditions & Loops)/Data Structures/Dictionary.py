

from datetime import date


services = {"service_name": "ec2",
            "service_cost": "$20",
            "Service_desc": "This is AWS"
            }

print(services["Service_desc"])


## Days of the week

days_of_week  = ("sun","mon","tue","wed","thu","fri","sat")    #tuple = cannot change (immutable)
days_of_week2 = ["sun","mon","tue","wed","thu","fri","sat"]    #list  = Can change (mutable)
date_1          = {1,1,1,1}                                    #set   = Cannot store duplicates


days_of_week[0] = "next"
days_of_week2[0] = "next"

print(date_1)

