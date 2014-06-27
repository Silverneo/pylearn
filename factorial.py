#!usr/bin/python

import sys

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = input("Please enter a number: ")
    if num < 0:
        print "Number should be positive!"
        sys.exit()
    product = factorial(num)
    print "{}! = {} by recursion".format(num, product)
    product = 1
    for i in range(1, num + 1):
        product = product * i
    print "{}! = {} by loop".format(num, product)


if __name__ == "__main__":
    main()
