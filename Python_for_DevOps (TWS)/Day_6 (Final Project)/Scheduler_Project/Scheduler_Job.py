import schedule
import time

def say_hi():
    print("Hi Everyone!")

schedule.every(5).seconds.do(say_hi)

while True:
    schedule.run_pending()
    time.sleep(1)