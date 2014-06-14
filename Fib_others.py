#!/usr/bin/python
#Fibonacci Sequence - Enter a number and have the program 
#generate the Fibonacci sequence to that number or to the Nth number.
print "This program generates the Fibonacci sequence to the Nth number."

n = 0
while(n == 0):
    try:
        n = int(raw_input("Choose n, an integer: "))
    except ValueError:
        print "That wasn't an integer, idiot. Try again."
    if n > 250000:
        print "Too big! Please enter an integer no more than 250000."
        n = 0
a = 1
b = 1
c = 0
while(n-2>0):
    c = b
    b = a + b
    a = c
    n = n - 1
    print b
