"""
Legal to Vote: Take user DOB as input. Verify if they can vote.
https://en.wikipedia.org/wiki/Voting_age
"""
from datetime import date, timedelta

# votingAge can be changed once, to be updated in the entire program
votingAge = 18

try:
    # If the user enters a junk value, it will result in Exception
    voterY, voterM, voterD = (input("Enter your DOB in yyyy-mm-dd format: ")).split("-")
    voterDOB = date(int(voterY), int(voterM), int(voterD))

except Exception as e:
    print("Resulted in error: ",e)

else:
    today = date.today()
    #timedelta() doesn't accept year as an argument, so have used days
    validDOB = today - timedelta(days=int(votingAge * 365.2425))

    if validDOB >= voterDOB:
        print("You are eligible to vote")
    else:
        votingDate = voterDOB + timedelta(days=int(votingAge * 365.2425))
        print("Person born on/after,", validDOB, "is eligible to Vote.")
        print("You are Ineligible to Vote. You can vote from: ", votingDate)