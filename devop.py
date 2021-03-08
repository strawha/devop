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
        z = square_root(y)
        print(z)
    elif (x == 2):
        y = int(input("enter the number for factorial: "))
        z = factorial(y)
        print(z)
    elif (x == 3):
        y = int(input("enter the number for natural log: "))
        z = natural_log(y)
        print(z)
    else:
        y = int(input("enter the first number: "))
        y = int(input("enter the second number: "))
        z = power(x,y)
        print(z)

    logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(x)
    logging.info(z)
