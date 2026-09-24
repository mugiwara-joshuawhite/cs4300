'''
task3.py
collection of math-related functions
'''

# imports
from math import pi, sqrt

def sign_of_num(n) -> str:
    '''
    sign_of_num
    returns what the sign of a number is
    '''

    if n > 0:
        return "+"
    if n == 0:
        return "0"
    if n < 0:
        return "-"

def first_10_prime():
    '''
    first_10_prime
    finds and prints the first 10 prime numbers
    '''

    # variables
    x = 1   # number to test for primeess
    primes = list() # list of found primes

    # loop 10 times
    for i in range(1, 11):

        # assume not prime
        xisprime = False

        # go until find another prime
        while xisprime == False:

            # test next number for primeness
            x += 1
        
            # assume this time it will be prime
            assumeprime = True

            # loop until sqrt(x) (any numbers past that have been covered)
            for j in range(2, int(sqrt(x)) + 1):

                # divide test number by another number
                y = x / j
                
                # see if the division is clean
                if y.is_integer():
                    assumeprime = False

                    # now know is not prime, can leave
                    break
            xisprime = assumeprime

        primes.append(x)

    print(primes)

def sum_1_to_100():
    '''
    sum_1_to_100
    finds the sum from 1 to 100
    '''
    sum = 0;
    for i in range(1, 101):
        sum += i
    return sum