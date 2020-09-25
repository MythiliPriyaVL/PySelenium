
fileLoc = "C:\\Users\\Mythili\\PycharmProjects\\SDET-Py-Jan2020\\venv\\ProgramCode\\TestData.txt"

i = 10 # variable, store simple data
i = "kk" #

myFile = open(fileLoc)
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())

print(myFile.read())

for eachLine in myFile:
    print(eachLine)

#r is for read only mode.
fileLoc1 = open("C:\\Users\\Mythili\\PycharmProjects\\SDET-Py-Jan2020\\venv\\ProgramCode\\TestData.txt", "r")
print(fileLoc1.read())

#a is for append mode, appends to the last
fileLoc1 = open("C:\\Users\\Mythili\\PycharmProjects\\SDET-Py-Jan2020\\venv\\ProgramCode\\TestData.txt", "a")
fileLoc1.write("\nWrite new line")
fileLoc1.writelines("\nWrite first line", "\nWrite second line", "\nWrite third line")
fileLoc1.close()

#w is for write mode, overwrites the contents if the file exists or creates a new file
fileLoc1 = open("C:\\Users\\Mythili\\PycharmProjects\\SDET-Py-Jan2020\\venv\\ProgramCode\\TestData1.txt", "w")
fileLoc1.write("\nWrite new line")
fileLoc1.writelines("\nWrite first line", "\nWrite second line", "\nWrite third line")
fileLoc1.close()