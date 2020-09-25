"""
Assignment: Calculator application
I/P: Enter 2 numbers, Enter an Operator
O/P: Result of the operation
"""

inp1 = float(input("Enter the 1st Number: "))
inp2 = float(input("Enter the 2nd Number: "))
operatorIP = input("Enter any one of the Operator (+,-,*,/,sqr): ")

output = 0.0

if (operatorIP == '+'):
    output = inp1 + inp2
elif (operatorIP == '-'):
    output = inp1 - inp2
elif (operatorIP == '*'):
    output = inp1 * inp2
elif (operatorIP == '/'):
    output = inp1 / inp2
elif (operatorIP.upper() == 'SQR'):
    output = inp1 ** inp2
else :
    print("You entered an Invalid Operator")

print(str(inp1) + operatorIP + str(inp2) + ' = ' + str(output))

# single line conditional statements
anyDay = input("Enter the day (Sun/Mon/Tue/Wed/Thu/Fri/Sat): ")
if (anyDay.casefold() == "mon" or anyDay.casefold() == "tue" or anyDay.casefold() == "wed" or anyDay.casefold() == "thu" or anyDay.casefold() == "fri" or anyDay.casefold() == "sat" or anyDay.casefold() == "sun"):
    output = "Weekday" if (anyDay.casefold() == "mon" or anyDay.casefold() == "tue" or anyDay.casefold() == "wed" or anyDay.casefold() == "thu" or anyDay.casefold() == "fri" ) else "Weekend"
    print(anyDay + " is a " + output)
else:
    print("Invalid input.")
