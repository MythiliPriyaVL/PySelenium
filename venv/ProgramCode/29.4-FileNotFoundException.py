"""
Write a script that handles opening a non-existing file, 'unknown_file.txt', and prints the message File not found. to the user.
Use try ... except clauses. Print the user message inside except clause.
"""


try:
    f = open("unknown_file.txt", "r")
    f.write("This is line 1 \r\n")
    f.close()
    
except FileNotFoundError:
    print("File not found")
"""
except Exception as errorMessage:
    print("Error message is: ", errorMessage)"""

