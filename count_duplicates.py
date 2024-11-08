# Write a function that will return the count of distinct case-insensitive alphabetic characters and 
# numeric digits that occur more than once in the input string. The input string can be assumed to 
# contain only alphabets (both uppercase and lowercase) and numeric digits. 

def count_duplicates(s):
    sd = {}
    count = 0
    s_lower = s.lower()

    for i in s_lower:
        if (i in sd):
            sd[i] += 1
        else:
            sd[i] = 1

    for k,v in sd.items():
        if sd[k] > 1:
            count += 1

    return count
    

print(count_duplicates(input("Enter a string ")))