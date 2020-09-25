#Program to print Fibonacci series, from and to value to be provided by End User
fibInputFrom = int(input("Enter the number from which Fibonacci series to be printed : "))
fibInputTo = int(input("Enter the number to which Fibonacci series to be printed : "))
fibonacciSeries = []
fibonacciSeries.append(0)
fibonacciSeries.append(1)

if(fibInputFrom<fibInputTo):
    for i in range(fibInputTo - 1) :
        fibonacciSeries.append(fibonacciSeries[i+1] + fibonacciSeries[i])

    print("Fibonacci serires: ", fibonacciSeries)
    # slicing - list[start:end:step]
    print("Fibonacci series: From", fibInputFrom, "To", fibInputTo, ": ", fibonacciSeries[fibInputFrom:(fibInputTo+1)])
    #print("Fibonacci series: From", fibInputFrom, "To", fibInputTo, ": ", fibonacciSeries[fibInputFrom:])
else:
    print("From - To range is not as per the requirement")