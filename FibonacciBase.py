#  File: FibonacciBase.py

#  Description: Program converts user input into binary, according to fib seq

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 11/09/2015

#  Date Last Modified: 11/09/2015

# main function gets user input
def main():
    number = int(input("Enter a number: "))
    print(number, "=", convert_fib_to_bin(number), "(fib)")

# convert fibonacci sequence to binary
def convert_fib_to_bin(n):
    # no need to continue if n = 0 
    if (n == 0):
        return 0
    else:
        # create new fib bin str
        fib_bin = ""
        x = 1
        
        # increment up to find starting point x
        while (not fib(x) > n):
            x = x + 1
        x = x - 1
        
        while (x > 0):
            if (not n < fib(x)):
                n = n - fib(x)
                fib_bin = fib_bin + "1"
            else:
                fib_bin = fib_bin + "0"
            x = x - 1
        return fib_bin

# recursion for fib seq
def fib(n):
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

'''
n       0   1   2   3   4   5   6   7   8   9   10
Fib(n)  0   1   1   2   3   5   8   13  21  34  55
'''
main()