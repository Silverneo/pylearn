#!/usr/bin/python
# Fibonacci Sequence Generation

def genFib():
    a = b = 1
    yield a
    yield b
    while True:
        b = a + b
        a = b - a
        yield b

def main():
    n = input("Input the number of Fibonacci Sequence: ")
    generator = genFib()
    for i in range(n):
        print generator.next(),

if __name__ == '__main__':
    main()
