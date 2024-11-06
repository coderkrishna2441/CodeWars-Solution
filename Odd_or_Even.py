# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero)

def odd_or_even(arr):
    sum = 0
    result = ""
    if len(arr) > 0:
        for digit in arr:
            sum += digit
        if sum%2 == 0:
            result = "even"
        else:
            result = "odd"
    else:
        result = "even"
    return result