"""
1. Create a list of bank users (3 users)
2. Each user should have A/C id, Pwd, Balance:
3. User must login with providing right credentials
4. After login, user can
    - check balance
    - add money
    - transfer to other user
    - withdraw
use: Loops, Lists, Functions
"""
#Initializing the User accounts
user1 = ["firstuser", "qwert!", 25000.00]
user2 = ["seconduser", "asdfg@", 155000.00]
user3 = ["thirduser", "zxcvb()", 3240.00]
#Multi-Dimensional Lists initialization
loginDetails = [user1, user2, user3]
appCheck = 'Y'

#Function to perform the user operations
def bankFunctions(userDetails):
    opCheck = 'Y'
    while (opCheck.upper() == 'Y') :
        operDetails = input("\nWhat do you want to perform? \n CB - Check Balance, AM - Add Money, TR - Transfer, WD - Withdraw, ET - Exit: ")

        #Check Balance of the account
        if (operDetails.upper() == 'CB'):
            print("Available Balance is : ", userDetails[2])

        #Add money to the account
        elif (operDetails.upper() == 'AM'):
            addAmount = float(input("How much do you want to add to the account : "))
            userDetails[2] += addAmount
            print("Updated balance is : ", userDetails[2])

        #Transfer money from the Account
        elif (operDetails.upper() == 'TR'):
            trfAccount = input("Enter the User Id of the account to which you like to transfer amount: ")
            for i in range(len(loginDetails)):
                #Checking the Account which matches the To account
                if(trfAccount ==loginDetails[i][0]):
                    toAccount = loginDetails[i]
                    # Transfer 'From' and 'To' account cannot be the same
                    if (trfAccount == userDetails[0]):
                        print("You cannot transfer to the same account")
                        break
                    else:
                        trfAmount = float(input("How much do you want to transfer : "))
                        #Amount to transfer should be less than or equal to existing balance
                        if(trfAmount <= userDetails[2]):
                            userDetails[2] -= trfAmount
                            toAccount[2] += trfAmount
                            print("Updated balance in From account is : ", userDetails[2])
                            #print("Updated balance in To account is : ", toAccount[2])
                            break
                        else:
                            print("Entered amount", trfAmount ,"is greater than the account balance ",userDetails[2])
                            break
            else:
                print("Entered account ID is not valid.")

        #Withdraw money from the account
        elif (operDetails.upper() == 'WD'):
            wdAmount = float(input("How much do you want to Withdraw from the account : "))
            if (wdAmount <= userDetails[2]):
                userDetails[2] -= wdAmount
                print("Updated balance is : ", userDetails[2])
            else:
                print("Entered amount", wdAmount, "is greater than the account balance ", userDetails[2])

        #Exit from the account or Logged out of the account
        elif (operDetails.upper() == 'ET'):
            print("Logged out of the User account : ", userDetails[0])
            break

        #Error should be displayed if the user provides wrong input
        else:
            opCheck = input("You have entered an invalid operation, do you want to try again? Y / N : ")
    else:
        print("Logged out of the User account : ", userDetails[0])


# Loop continues until the user wants to terminate the application
while(appCheck.upper() == 'Y'):
    userId = input("\nEnter the User Id of the account: ")

    #If the input matches user1, below statements will be executed
    if (userId.lower() == user1[0]):
        pwDetails = input("Enter the Password of the account: ")
        if (pwDetails == user1[1]):
            bankFunctions(user1)
        else:
            print("Entered Password does not match the account.")

    # If the input matches user2, below statements will be executed
    elif (userId.lower() == user2[0]):
        pwDetails = input("Enter the Password of the account: ")
        if (pwDetails == user2[1]):
            bankFunctions(user2)
        else:
            print("Entered Password does not match the account.")

    # If the input matches user3, below statements will be executed
    elif (userId.lower() == user3[0]):
        pwDetails = input("Enter the Password of the account: ")
        if (pwDetails == user3[1]):
            bankFunctions(user3)
        else:
            print("Entered Password does not match the account.")

    # If the input doesn't match any of the existing users, error message will be displayed.
    else:
        print("Entered UserId does not match any of the account.")

    # Application continues until the user specifies 'N'
    appCheck = input("Do you want to continue ? Y / N : ")
else:
    print("Terminating the app.")


