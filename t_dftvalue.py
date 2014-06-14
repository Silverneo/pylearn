def foo(bar = []):
    bar.append("baz")
    return bar
# python's default argument for function is only evaluated when def is executed
# first time.

def foo1(bar = None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar


print 'first call'
print foo()

print 'second call'
print foo()

print 'third call'
print foo()
