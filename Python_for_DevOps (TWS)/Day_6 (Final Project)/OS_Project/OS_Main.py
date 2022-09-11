import os
import time
import shutil
import logging
import datetime as dt

logging.basicConfig(filename="logs.txt", level="INFO")
while True:
    
    total,used,free = shutil.disk_usage("/")

    used_prct = (used/total)*100
    free_prct = (free/total)*100

    if   free_prct < 15:
            print("Free karo")
            logging.critical("Email Alert Sent!")
    elif free_prct > 40 and free_prct < 70:
            print("Free hain")
            logging.error("Email Alert to be Sent!")
    else:
            print("Bhar do bhai please")
    time.sleep(3)
