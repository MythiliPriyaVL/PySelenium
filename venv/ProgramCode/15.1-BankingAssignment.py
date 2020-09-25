"""
1. Create a list of bank users (3 users)
2. Each user should have A/C id, Pwd, Balance:
3. User must login with providing right credentials
4. After login, user can
    - Check balance
    - Deposit money
    - Transfer money to other user
    - Withdraw money
use: Loops, Lists, Functions
"""

#Initializing the User accounts
#Multi-Dimensional Lists initialization
userDetails = [["firstuser", "qwert!", 25000.00], ["seconduser", "asdfg@", 155000.00], ["thirduser", "zxcvb()", 3240.00]]
appCheck = 'Y'

def depositMoney(userNumber):
    # Function to perform Deposit Amount in the user account
    addAmount = float(input("How much do you want to add to the account : "))
    userDetails[userNumber][2] += addAmount
    print("Updated balance is : ", userDetails[userNumber][2])


def withdrawMoney(userNumber):
    # Function to perform Withdraw Amount from the user account
    wdAmount = float(input("How much do you want to Withdraw from the account : "))
    if (wdAmount <= userDetails[userNumber][2]):
        userDetails[userNumber][2] -= wdAmount
        print("Updated balance is : ", userDetails[userNumber][2])
    else:
        print("Entered amount", wdAmount, "is greater than the account balance ", userDetails[userNumber][2])


def transferMoney(userNumber):
    # Function to perform Transfer Amount from the user account to Another account
    trfAccount = input("Enter the User Id of the account to which you like to transfer amount: ")
    for i in range(len(userDetails)):
        # Checking the Account which matches the To account
        if (trfAccount == userDetails[i][0]):
            toAccount = userDetails[i]
            # Transfer 'From' and 'To' account cannot be the same
            if (trfAccount == userDetails[userNumber][0]):
                print("You cannot transfer to the same account")
                break
            else:
                trfAmount = float(input("How much do you want to transfer : "))
                # Amount to transfer should be less than or equal to existing balance
                if (trfAmount <= userDetails[userNumber][2]):
                    userDetails[userNumber][2] -= trfAmount
                    toAccount[2] += trfAmount
                    print("Updated balance in From account is : ", userDetails[userNumber][2])
                    # print("Updated balance in To account is : ", toAccount[2])
                    break
                else:
                    print("Entered amount", trfAmount, "is greater than the account balance ", userDetails[userNumber][2])
                    break
    else:
        print("Entered account ID is not valid.")


def bankFunctions(userNumber):
    # Function to perform the user operations
    opCheck = 'Y'
    while (opCheck.upper() == 'Y') :
        operDetails = input("\nWhat do you want to perform? \n CB - Check Balance, DM - Deposit Money, TR - Transfer, WD - Withdraw, ET - Exit: ")
        #Check Balance of the account
        if (operDetails.upper() == 'CB'):
            print("Available Balance is : ", userDetails[userNumber][2])
        #Add money to the account
        elif (operDetails.upper() == 'DM'):
            depositMoney(userNumber)
        #Transfer money from the Account
        elif (operDetails.upper() == 'TR'):
            transferMoney(userNumber)
        #Withdraw money from the account
        elif (operDetails.upper() == 'WD'):
            withdrawMoney(userNumber)
        #Exit from the account or Logged out of the account
        elif (operDetails.upper() == 'ET'):
            print("Logged out of the User account : ", userDetails[userNumber][0])
            break
        #Error should be displayed if the user provides wrong input
        else:
            opCheck = input("You have entered an invalid operation, do you want to try again? Y / N : ")
    else:
        print("Logged out of the User account : ", userDetails[userNumber][0])


# Loop continues until the user wants to terminate the application
while(appCheck.upper() == 'Y'):
    userId = input("\nEnter the User Id of the account: ")
    for i in range(len(userDetails)):

        if (userId.lower() == userDetails[i][0]):
            pwDetails = input("Enter the Password of the account: ")
            if (pwDetails == userDetails[i][1]):
                print("Hello,",userDetails[i][0].upper(),"Welcome!")
                bankFunctions(i)
                break
            else:
                print("Entered Password does not match the account.")
                break
    else:
        print("Entered UserId does not match any of the account.")

    # Application continues until the user specifies 'N'
    appCheck = input("Do you want to continue ? Y / N : ")
else:
    print("Terminating the app.")