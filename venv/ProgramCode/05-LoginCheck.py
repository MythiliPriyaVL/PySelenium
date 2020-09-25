"""
Login Testing:
1. User Name and Password are hardcoded in the program
2. User should enter right combination of values to login
3. User can try upto 3 times and the program stops after that.
"""

#Hardcoded User Name and Password values
uN1 = "newUser"
uP1 = "09876"

#Looping for 3 maximum attempts
for x in range(3):
    #User Input for User Name and Password
    uName = input("Enter the User Name: ")
    uPassword = input("Enter the Password: ")

    if(uN1 == uName and uP1 == uPassword):
        print("User login Successful.")
        print("Access granted")
        break
    else:
        print("User login Unsuccessful.")
        print("Access Denied")
else:
    print("Maximum attempts reached. Try after sometime.")