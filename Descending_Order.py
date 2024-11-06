# Your task is to make a function that can take any non-negative integer as an argument and return 
# it with its digits in descending order. Essentially, rearrange the digits to create the highest 
# possible number.

def descending_order(num):
    # Bust a move right here
    digits = []
    new_number = ""
    for digit in str(num):
        digits.append(digit)
        
    for i in range(len(digits)-1,0,-1):
        for j in range(i):
            if digits[j] < digits[i]:
                temp = digits[i]
                digits[i] = digits[j]
                digits[j] = temp
        
    for d in digits:
        new_number += d
         
    return int(new_number)