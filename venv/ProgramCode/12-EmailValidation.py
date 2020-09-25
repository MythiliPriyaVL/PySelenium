#6. Write a program to check if an entered email address is valid or not.
"""
Valid email address format
1. Acceptable email prefix formats
Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
An underscore, period, or dash must be followed by one or more letter or number.
2. Acceptable email domain formats
Allowed characters: letters, numbers, dashes.
The last portion of the domain must be at least two characters, for example: .com, .org, .cc
"""

emailInput = input("Enter the Email address to Validate : ")

#Checking number of times @ symbol is used in the email address
if(emailInput.count("@") > 1):
    print("Not a valid email address, cannot have more '@' symbol in an email address.")
elif(emailInput.count("@") == 0):
    print("Not a valid email address, should have '@' symbol before domain name in an email address.")
else:
    # for anyone@gmail.com; x = ('anyone','@','gmail.com')
    x = emailInput.partition("@")
    #domain validation
    if (x[2].count(".") == 1):
        # y = ('gmail','.','com')
        y = x[2].partition(".")
        print(x)
        print(y)
        if(len(y[0])>=2 and len(y[2])>=2):
            if(len(x[0])>=1):
                print("Valid Email address")
            else:
               print("Not a valid email address, prefix cannot be blank.")
        else:
            print("Not a valid email address, domain details cannot be blank.")
    else:
        print("Not a valid email address, should have one '.' symbol in the domain name in an email address.")

"""
#Checks for Alphanumberic, gives true if the UserId part is alphanumeric
        z = x[0].isalnum()
        print(z)
#Finds the position of the given string/Character
        x = emailInput.find("@")
        print(x)
        y = emailInput.find(".")
        print(y)
        #Checks whether the email ends with .com
        z = emailInput.endswith(".com")
        print(z)
"""