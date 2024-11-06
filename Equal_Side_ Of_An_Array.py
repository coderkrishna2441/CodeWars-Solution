# You are going to be given an array of integers. 
# Your job is to take that array and find an index N where the sum of the integers to the left of 
# N 
# is equal to the sum of the integers to the right of N.

# If there is no index that would make this happen, return -1.

def find_even_index(arr):
    for i in range(len(arr)):
        sum1 = 0
        sum2 = 0
        for j in range(0,i):
            sum1 += arr[j]
        for k in range(i+1,len(arr)):
            sum2 += arr[k]
        if sum1 == sum2:
            N = i
            break
        else:
            N = -1
    return N