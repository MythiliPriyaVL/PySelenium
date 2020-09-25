"""
Write a script that reads an integer from STDIN and raise ValueError exception if the number is not between 0 and 100.
The message to user must be : "Input integer value must be between 0 and 100."
Use try... except clauses. Specify the error message inside except clause.
Provide 200 as input while executing the script.
"""


try:
    intValue = int(input("Enter the integer : "))
    if(intValue>0 and intValue<100):
        print("Your input value {} is acceptable.",format(intValue))
    else:
        raise ValueError

except ValueError:
    print("Input integer value must be between 0 and 100.")
