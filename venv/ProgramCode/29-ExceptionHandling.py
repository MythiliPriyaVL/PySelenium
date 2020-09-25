#Exception Handling examples

#The try block lets you test a block of code for errors
try:
    #print(x)
    tInt = 10
    tDiv = 1
    divResult = tInt/tDiv
    print("Division result is: ", divResult)

except NameError:
  print("Variable x is not defined")

#The except block lets you handle the error.
except Exception as errorMessage:
    print("Error message is: ", errorMessage)

else:
    print("Random try of checking else block")

#The finally block lets you execute code, regardless of the result of the try- and except blocks.
finally:
    print("Will be executed irrespective of error.")


"""
You can also handle multiple exceptions using a single except clause by passing these exceptions to the clause as a tuple . 
except (ZeroDivisionError, ValueError, TypeError): print ( "Something has gone wrong.." )
"""
