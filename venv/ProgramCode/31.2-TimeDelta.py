#Example file for timedelta
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

def main():
    # basic timedelta
    print(timedelta(days=365, hours=5, minutes=1))

    #Today's date
    now = datetime.now()
    print("Today is: ", str(now))

    #Today's date one year from now
    print("One year from now, it will be: ", str(now+timedelta(365)))

    # timedelta with more argument
    print("In 2 days and 3 weeks, it will be: ", str(now + timedelta(days=2, weeks=3)))

    #Calculate Date 1 week ago, formatted as a String
    t= datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was: ", s)

    #How many days until April fool's day
    today = date.today()
    afd = date(today.year, 4, 1) #2020-04-01
    #Check if the April Fool's day already went by
    if afd < today:
        print("April fool's day already went by %d days ago" %((today-afd).days))
        afd =  afd.replace(year = today.year+1)

    time_to_afd = afd-today
    print("It's just ", time_to_afd.days," days until April Fool's day")

    print(timedelta.max)
    print(timedelta.min)
    print(timedelta.resolution)

if __name__ =="__main__":
    main();