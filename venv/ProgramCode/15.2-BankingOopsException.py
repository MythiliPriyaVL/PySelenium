"""
Re-Do Banking Assignment: Using OOP and Try-Except-Final
"""
class userInformation:
    def __init__(self,uId,uPw,uBal):
        self.uId = uId
        self.uPw = uPw
        self.uBal = uBal

    def depositMoney(self):
        # Function to perform Deposit Amount in the user account
        addAmount = float(input("How much do you want to add to the account : "))
        self.uBal += addAmount
        print("Updated balance is : ", self.uBal)

    def withdrawMoney(self):
        # Function to perform Withdraw Amount from the user account
        wdAmount = float(input("How much do you want to Withdraw from the account : "))
        if (wdAmount <= self.uBal):
            self.uBal -= wdAmount
            print("Updated balance is : ", self.uBal)
        else:
            print("Entered amount", wdAmount, "is greater than the account balance ", self.uBal)

    def transferMoney(self):
        # Function to perform Transfer Amount from the user account to Another account
        trfAccount = input("Enter the User Id of the account to which you like to transfer amount: ")
        for i in range(len(userDetails)):
            # Checking the Account which matches the To account
            if (trfAccount == userDetails[i].uId):
                toAccount = userDetails[i]
                # Transfer 'From' and 'To' account cannot be the same
                if (trfAccount == self.uId):
                    print("You cannot transfer to the same account")
                    break
                else:
                    trfAmount = float(input("How much do you want to transfer : "))
                    # Amount to transfer should be less than or equal to existing balance
                    if (trfAmount <= self.uBal):
                        self.uBal -= trfAmount
                        toAccount.uBal += trfAmount
                        print("Updated balance in From account is : ", self.uBal)
                        # print("Updated balance in To account is : ", toAccount[2])
                        break
                    else:
                        print("Entered amount", trfAmount, "is greater than the account balance ",self.uBal)
                        break
        else:
            print("Entered account ID is not valid.")

    def bankFunctions(self):
        # Function to perform the user operations
        opCheck = 'Y'
        while (opCheck.upper() == 'Y'):
            operDetails = input(
                "\nWhat do you want to perform? \n CB - Check Balance, DM - Deposit Money, TR - Transfer, WD - Withdraw, ET - Exit: ")
            # Check Balance of the account
            if (operDetails.upper() == 'CB'):
                print("Available Balance is : ", self.uBal)
            # Add money to the account
            elif (operDetails.upper() == 'DM'):
                self.depositMoney()
            # Transfer money from the Account
            elif (operDetails.upper() == 'TR'):
                self.transferMoney()
            # Withdraw money from the account
            elif (operDetails.upper() == 'WD'):
                self.withdrawMoney()
            # Exit from the account or Logged out of the account
            elif (operDetails.upper() == 'ET'):
                print("Logged out of the User account : ", self.uId)
                break
            # Error should be displayed if the user provides wrong input
            else:
                opCheck = input("You have entered an invalid operation, do you want to try again? Y / N : ")
        else:
            print("Logged out of the User account : ", self.uId)


#Initializing the User accounts
u1 = userInformation("firstuser", "qwert!", 25000.00)
u2 = userInformation("seconduser", "asdfg@", 155000.00)
u3 = userInformation("thirduser", "zxcvb()", 3240.00)

userDetails =[u1,u2,u3]

appCheck = 'Y'

# Loop continues until the user wants to terminate the application
while(appCheck.upper() == 'Y'):
    userId = input("\nEnter the User Id of the account: ")
    for i in range(len(userDetails)):

        if (userId.lower() == userDetails[i].uId):
            pwDetails = input("Enter the Password of the account: ")
            if (pwDetails == userDetails[i].uPw):
                print("Hello,",userDetails[i].uId.upper(),"Welcome!")
                userDetails[i].bankFunctions()
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