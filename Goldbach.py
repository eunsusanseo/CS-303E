#  File: Goldbach.py

#  Description: verify Goldbach's conjecture in a user defined range

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 9/20/15

#  Date Last Modified: 9/21/15

#  Self-Note: Please disregard


# check if num is prime
def is_Prime(num):

    divisor = 2
    limit = int(num // 2 + 1)

    while (divisor < limit):
        if (num % divisor == 0):
            return False
        else: 
            divisor = divisor + 1
    return True

def main():
    # Declare variables
    lower = 0
    upper = 0
    max_count = 0

    # Ask user for lower and upper limit input
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))

    # Set error checking bounds, if invalid, prompt user for input again
    while((lower < 4) or (upper < 4) or (lower > upper) or (lower % 2 != 0) or (upper % 2 != 0)):
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))

    # Check while within lower to upper range
    while (lower <= upper):
        a = 2
        n = lower
        counter = 0 

        # First print lower number so you don't lose it
        print("\n", lower, end = ' ') # Self-Note: (end = ' ') does not send to new line, built in function

        while (a <= n // 2):
            b = n - a
            if is_Prime(a): # Self-Note: if is_Prime returns true (from top), enter 1st if loop
                if is_Prime(b): # Note: if is_Prime returns true (from top), enter 2nd if loop
                    print("=", a, "+", b, end = ' ') # Note: Use (end = ' ') to keep adding additional "= a + b" outputs
                    counter += 1
            a += 1 # Self-Note: keep adding 1 to a and checking if a and b prime as long as (a <= n //2)

        # Find maximum number of pairs
        if (counter > max_count):
            max_count = counter

        lower += 2

    print()   
main()
