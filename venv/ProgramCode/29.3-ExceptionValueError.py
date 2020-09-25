"""
Write a script that reads a string from STDIN and
raise ValueError exception if the string has more than 10 characters or else prints the read string.
The message to user must be : "Input String contains more than 10 characters."
Use try ... except clauses. Print the error message inside except block.
Provide 'PythonIsAmazing' as input string while executing the string.
"""

try:
    strValue = input("Enter the string : ")
    if(len(strValue)<=10):
        print("Your input string, {} is acceptable.",format(intValue))
    else:
        raise ValueError

except ValueError:
    print("Input String contains more than 10 characters.")