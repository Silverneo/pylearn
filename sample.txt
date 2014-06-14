import sys

output = 'hello world!'
if len(sys.argv) == 2:
    print output[-1:-6:-1] + sys.argv[1]
else:
    print output
