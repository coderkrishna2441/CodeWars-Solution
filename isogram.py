# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case. 

def isIsogram(word):
    d = {}
    flag = True

    if len(word) > 0:
        words = word.lower()
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    else:
        flag = True

    for k,v in d.items():
        if v == 1:
            flag = True
        else:
            flag = False
            break

    return True if flag else False

print(isIsogram(input("Enter a word ")))