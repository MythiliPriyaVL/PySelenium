#Example file for Date Formatting
from datetime import datetime


def main():
    now=datetime.now()
    ### DATE FORMATTING ###
    print(now.strftime("Current year is: %Y")) #Current year is: 2020

    # %y/%Y - Year, %a/%A - Weekday, %b/%B - month, %d - day of month
    print(now.strftime("%a, %d %B, %y")) #Thu, 27 February, 20

    # %c - Local date and time, %x - local date, %X - local time
    print(now.strftime("Local date and time: %c")) #Local date and time: Thu Feb 27 18:33:35 2020
    print(now.strftime("Local date: %x"))
    print(now.strftime("Local time: %X"))

    ### TIME FORMATTING ###
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - Local AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))

if __name__ =="__main__":
    main();