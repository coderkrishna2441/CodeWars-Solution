# Write a function that takes an integer as input, and returns the number of bits that are equal to 
# one in the binary representation of that number. You can guarantee that input is non-negative.

def count_bits(n):
    count = 0
    while n >= 1:
        
        if int(n%2) == 1:
            count += 1
        n = n/2
    return count