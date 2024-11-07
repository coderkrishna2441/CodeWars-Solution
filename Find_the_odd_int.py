# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    for k,v in d.items():
        if v%2 != 0:
            return k
    