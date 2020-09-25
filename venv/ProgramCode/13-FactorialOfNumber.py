# Program to print Factorial of the number, input provided by End User

factInput = int(input("Enter the number for which Factorial to be calculated: "))
factOutpt = 1

for i in range(1,factInput+1):
    factOutpt = i * factOutpt

print("Factorial of ", factInput, " is : ", factOutpt)