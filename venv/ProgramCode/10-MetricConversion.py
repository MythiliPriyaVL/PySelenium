#3. Write a program that converts temperatures. C to F and other way.
#4. Write a program that converts heights. Meters to Feet and Inches and vice versa.

# Function to perform the Temperature Conversion
def tempFunction():
    converInput = input("If you want to convert from Celcius to Fahrenheit, type (CF); or Fahrenheit to Celcius, type (FC) : ")
    if (converInput.upper() == 'CF'):
        tempInput = float(input("Enter the Celcius value : "))
        tempOutput = float((tempInput * 9) / 5) + 32
        # for typing ° symbol use (alt+0176) or (fn+0176)
        print(str(tempInput) + "° Celcius is " + str(tempOutput) + "° Fahrenheit")
    elif (converInput.upper() == 'FC'):
        tempInput = float(input("Enter the Fahrenheit value : "))
        tempOutput = float((tempInput - 32) * 5 / 9)
        print(str(tempInput) + "° Fahrenheit is " + str(tempOutput) + "° Celcius")
        #print('%0.2f Fahrenheit is: %0.2f Celsius' %(tempInput, tempOutput))
    else:
        print("Accepted input values are CF, FC; you typed a wrong value")

# Function to perform the Height Conversion
def heightFunction():
    converInput = input("If you want to convert from Meter to Feet, type (MF); or Feet to Meter, type (FM) : ")
    if (converInput.upper() == 'MF'):
        heightInput = float(input("Enter the Meter value : "))
        heightOutput = round(heightInput * 3.281,2)
        hOpFeet = int((heightOutput * 100) / 100) # Seperating the Feet Value
        hOpInches = int((heightOutput * 100) % 100) * .12 # Converting to Inches
        print(str(heightInput) + " Meter is " + str(hOpFeet) + " Feet " + str(hOpInches) + " Inches")
    elif (converInput.upper() == 'FM'):
        heightInput = float(input("Enter the Feet value : "))
        heightOutput = round(heightInput / 3.281, 2)
        print(str(heightInput) + " Feet is " + str(heightOutput) + " Meter")
    else:
        print("Accepted input values are MF, FM; you typed a wrong value")

calcInput = 'Y'

while(calcInput == 'Y'):
    metricInput = input("What do you want to Convert? 1. Temperature 2. Heights ")
    if(metricInput.casefold() == "temperature"):
        tempFunction()
    elif(metricInput.casefold() == "heights"):
        heightFunction()
    else:
        print("Wrong Input, Try again.")
    calcInput = input("\nDo you want to continue Calculating? Y / N :")
