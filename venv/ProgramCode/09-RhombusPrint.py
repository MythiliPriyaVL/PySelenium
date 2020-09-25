"""
2. Print a rhombus like below
     ___.
     __._.
     _.___.
     ._____.
     _.___.
     __._.
     ___.
"""
# User Input for Rhombus Height
rhomHeight = int(input("Enter the Rhombus Height, value should be >= 3 and an Odd Number: "))

#Validating the User Input before proceeding to the For loop
if ((rhomHeight >= 3) and (rhomHeight%2 != 0)):
    #Printing the first half of the Rhombus
    for i in range(int(rhomHeight/2)+1) :
        if (i==0) : # for the tip of Rhombus only one "*" should be present
            print(" " * (int(rhomHeight / 2) + 1 - i) + "*" + " " * (i) + " " * (i - 1))
        else:
            print(" " * (int(rhomHeight / 2) + 1 - i) + "*" + " " * (i) + " " * (i - 1) + "*")
    #Printing the bottom half of Rhombus
    for i in range((int(rhomHeight/2))-1,-1,-1) :# Decrementing the value from the mid
        if (i==0) :
            print(" " * (int(rhomHeight / 2) + 1 - i) + "*" + " " * (i) + " " * (i + 1))
        else:
            print(" " * (int(rhomHeight / 2) + 1 - i) + "*" + " " * (i) + " " * (i - 1) + "*")
else:
    print("Entered value is not as per the input requirement, try again. ")
