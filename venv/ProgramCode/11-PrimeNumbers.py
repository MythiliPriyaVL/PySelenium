#5. Print prime numbers below a given number.
#Get input from the User and print whether the value is Prime or Not

numberInput = int(input("Enter any number, I can print the Prime Numbers below that :"))
#Validating the Input value
if (numberInput == 1 or numberInput == 2 ):
    print("There is no Prime Number below " + str(numberInput))

else:
    print("Prime numbers below " + str(numberInput) + " are: ")
    print("2")
    x = 1
    for num in range(3, numberInput,2):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            x = x + 1
            print(num)
print("Total number of prime numbers are: ", x)