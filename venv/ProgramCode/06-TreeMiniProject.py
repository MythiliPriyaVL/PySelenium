"""
Purpose: Print a Tree
Take Height : Eg 8
Take Width : Eg 7
Print like below:
            *
           ***
          *****
         *******
            *
            *
            *
            *
"""

# User Input for Tree Height and Tree Width
tHeight = int(input("Enter the Tree Height, value should be > 3: "))
tWidth = int(input("Enter the Tree Width, value should be >= 3: "))

#Validating the User Input before proceeding to the For loop
if (type(tHeight) == int and tHeight >3 and type(tWidth) == int and tWidth >= 3):

    #Calculating Tree Crown height and Trunk Height. If the given Height is an Odd Number, then making the Crown as (Tree Height/2) +1
    tCrown = int(tHeight / 2) if (tHeight % 2 == 0) else int((tHeight / 2) + 1)
    tTrunk = tHeight - tCrown

    #Calculating the Peak width; Diving the width into equal proportions
    tCInitialWidth = int(tWidth / tCrown)

    #Calculating the Adjustment to be done for the final Width, if the Width is Odd number
    tCInitialWidthAdj = 0 if (tWidth % tCrown == 0) else tWidth % tCrown

    #Printing the Crown of the Tree
    for hH in range(tCrown):
        tDisplayDummy = "*" * ((tCInitialWidth*(hH+1))+tCInitialWidthAdj) if hH == (tCrown-1) else "*" * (tCInitialWidth*(hH+1))
        tDisplay = " " * int((tWidth-len(tDisplayDummy))/2) + tDisplayDummy
        print(tDisplay)

    #Printing the Trunk of the Tree
    for h in range(tTrunk):
        tDisplay = " " * int(tWidth/2) + "*"
        print(tDisplay)
else:
    print("Entered input doesn't match the given criteria. Cannot draw a Tree, try with valid values.")