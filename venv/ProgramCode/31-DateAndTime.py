#Example file for working with date information

from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    print("Today's date is ", today)
    print("Date components: ", today.day, today.month, today.year)
    #0=Monday, 6=Sunday
    print("Today's weekday # is: ", today.weekday())
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("which is a :", days[today.weekday()])

    #DATETIME OBJECTS
    today = datetime.now()
    print("Current date and time is ", today)
    time = datetime.time(datetime.now())
    print("Current time is ", time)

if __name__ =="__main__":
    main();