"""
Convert a string to Camel Case.
 Example a. "can be Any STRING". Camel Case "canBeAnyString".
 Rule : All words lower case. 1st character of every word Upper Case, except the 1st word. Remove Spaces.

 title()	Converts the first character of each word to upper case
 capitalize()	Converts the first character to upper case
 casefold()	Converts string into lower case
"""


try:
    # If the user enters a junk value, it will result in Exception
    strInput = input("Enter the string to be converted to Camel case: ")
    res = isinstance(strInput, str)
    print(res)

except Exception as e:
    print("Resulted in error: ",e)

else:
    resStr = strInput.casefold().title().replace(" ","")
    resStr = resStr.replace(resStr[0],resStr[0].lower())
    print(resStr)