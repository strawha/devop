import logging
import math

def square_root(a):
    return math.sqrt(a)

def factorial(a):
    return math.factorial(a)

def natural_log(a):
    return math.log(a)

def power(a,b):
    return math.pow(a,b)

if __name__ == "__main__":
    x = int(input("enter your choice 1) for square root 2) for factorial 3) for natural_log 4) for power: "))
    if (x == 1):
        y = int(input("enter the number for square root: "))
        try:
            z = square_root(y)
            print(z)
        except ValueError:
            print("square root not possible for negative number")
            z = 0
    elif (x == 2):
        y = int(input("enter the number for factorial: "))
        try:
            z = factorial(y)
            print(z)
        except ValueError:
            print("factorial not defined for negative values")
            z = 0
    elif (x == 3):
        try:
            y = int(input("enter the number for natural log: "))
            z = natural_log(y)
            print(z)
        except ValueError:
            print("natural log only possible for number greater than zero")
            z = 0
    elif (x == 4):
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        z = power(a,b)
        print(z)
    else:
        print("you only have 4 choices to choose from")
        z = 0

    logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(x)
    logging.info(z))
