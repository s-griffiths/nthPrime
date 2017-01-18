# NthPrime.py
# Prompts the user for a positive whole number, N, and returns the Nth prime number.

# imports math library
import math

# checks if a number is prime and returns true or false
def isPrime(number):

    prime = True

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number%i == 0 and i != number:
            prime = False
            break
    return prime

# variable used to offer user option to run program multiple times before closing
repeat = True

# variable used to determine when to return the appropriate prime number
nPrimeNotFound = True

# variable used to count prime numbers
primeCounter = 0

# variable used to hold the first prime number
primeNumber = 2

# loop to offer user control of when to close the program
while repeat:

    # variable to hold user entered number = prime number being sought
    N = int(input("Enter a positive whole number: "))

    # requests that N is a positive whole number if the original N was not
    while N <= 0:
        N = int(input("Must be a POSITIVE WHOLE number: "))

    # loop to count prime numbers until the Nth prime number is found
    while nPrimeNotFound:
        if isPrime(primeNumber):
            primeCounter += 1
        if primeCounter == N:
            nPrimeNotFound = False
        else:
            primeNumber += 1

    # adjusts the tail of N for the ouput according to the number
    tail = None
    temp = N
    while temp > 9:
        temp %= 10
    if temp == 1:
        tail = "st"
    elif temp == 2:
        tail = "nd"
    elif temp == 3:
        tail = "rd"
    else:
        tail = "th"

    # prints the Nth prime number
    print("The", str(N) + tail, "prime number is", str(primeNumber) + ".")

    
    # user is asked if they want to run the program again or quit
    user = str(input("\nWould you like to find another prime number (y/n)? "))
    while user != "y" and user != "n":
        user = str(input("\nPlease enter 'y' to continue or 'n' to quit)? "))
    if user == "y":
        repeat = True
        nPrimeNotFound = True
        primeCounter = 0
        primeNumber = 2
    elif user == "n":
        repeat = False
    print()
        
            



