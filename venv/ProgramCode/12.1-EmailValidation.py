# Program to validate an Email

# import re module
# re module provides support for regular expressions
import re

# Make a regular expression for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

'''
if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
'''

# Define a function for validating an Email
def check(email):
    # pass the regualar expression
    # and the string in search() method
    if (re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

emailInput = input("Enter the Email address to Validate : ")
check(emailInput)