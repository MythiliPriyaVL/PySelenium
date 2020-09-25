#Example file for Calendar Formatting
import calendar

def main():
    # Create plain text calendar
    c= calendar.TextCalendar(calendar.SUNDAY)
    st = c.formatmonth(2020, 1, 0, 0)
    print(st)

    #Create HTML Calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2020, 1)
    print(st)

    #Loop over the days of a month
    # If there are 0's in the output, it means there are other month days in the week
    for i in c.itermonthdays(2020, 8):
        print(i)

    for name in calendar.month_name:
        print(name)

    for name in calendar.day_name:
        print(name)

    #Calculate days based on a rule
    print("Team meetings will be on: ")
    for m in range(1,13):
        cal = calendar.monthcalendar(2020, m)
        weekone = cal[0]
        weektwo = cal[1]
        if weekone[calendar.FRIDAY] != 0:
            meetDay = weekone[calendar.FRIDAY]
        else:
            meetDay = weektwo[calendar.FRIDAY]
        print("%10s %2d" %(calendar.month_name[m], meetDay))

if __name__ =="__main__":
    main();