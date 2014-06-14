from string import upper, join, split


def flip(s):
    a = list(s)     # make s a list of character
    a.reverse()     # reverse the list order
    return join(a,'')       # join the list of char and return

#normalize = lambda s: join(split(s), ' ')

fp0 = open('sample.txt', 'r')
fp1 = open('output.txt', 'w')

cap_flip_norms = map(upper, map(flip, fp0.readlines()))


fp1.writelines(cap_flip_norms)

fp0.close()
fp1.close()
