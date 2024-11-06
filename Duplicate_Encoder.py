# The goal of this exercise is to convert a string to a new string where each character in 
# the new string is "(" if that character appears only once in the original string, or ")" if that 
# character appears more than once in the original string. Ignore capitalization when determining if 
# a character is a duplicate.

def duplicate_encode(word):
    #your code here
    new_word = ""
    for letter in word.lower():
        if word.count(letter) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word