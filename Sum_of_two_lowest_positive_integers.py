# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 
# 4 positive integers. No floats or non-positive integers will be passed.

def sum_two_smallest_numbers(numbers):
    #your code here
    smallest = numbers[0]
    second_smallest = numbers[1]
    sum = 0
     
    for i in range (len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    for j in range(len(numbers)):
        if numbers[j] < second_smallest and numbers[j] > smallest:
                second_smallest = numbers[j]
        sum = smallest + second_smallest
    return sum