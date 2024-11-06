# You will be given an array of numbers. You have to sort the odd numbers in ascending order while 
# leaving the even numbers at their original positions.

def sort_array(source_array):
    for i in range(len(source_array)-1,0,-1):
        if source_array[i]%2 != 0:
            for j in range(i):
                if source_array[j]%2 != 0:
                    if source_array[i] < source_array[j]:
                        temp = source_array[i]
                        source_array[i] = source_array[j]
                        source_array[j] = temp
    return source_array