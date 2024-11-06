# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second 
# character of the final pair with an underscore ('_').

def solution(s):
    if len(s)%2 != 0:
        s += "_"
    new_s = []
    index = 0
    for i in range(int(len(s)/2)):
        new_s.append(s[index] + s[index+1])
        index += 2
    return new_s