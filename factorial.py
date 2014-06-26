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
    n = num
    while num > 1:
        product = num * product
        num = num - 1
    print "{}! = {} by loop".format(n, product)


if __name__ == "__main__":
    main()
