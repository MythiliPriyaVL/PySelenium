#Example file for working with Loops

x=0

#Define a While loop
while(x<5):
    print(x)
    x = x+1

#Define a For loop
for x in range(5,10):
    print(x) #O/P:5,6,7,8,9

#Define a For loop with Range with an increment
for x in range(10,30,2):
    print(x) #O/P:10,12,14...28

#Use a For loop over a collection
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for d in days:
    print(d)

#Use the Break and Continue statements
for x in range(10,30):
    if(x == 25): break
    if(x % 2 == 0): continue # Loop continues for next x value for Even numbers
    print(x)

#using the enumerate() function to get index
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
"""
for i in range(len(days)):
    print(i,days[i])
"""
for i,d in enumerate(days):
    print(i, d)

