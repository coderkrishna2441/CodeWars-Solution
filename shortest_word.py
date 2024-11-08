# Simple, given a string of words, return the length of the shortest word(s)
# String will never be empty and you do not need to account for different data types. 

def shortest_word(sentence):
    words = sentence.split(" ")
    length = [] 
    
    for i in words:
        length.append(len(i))

    shortest = length[0]
    for j in range(len(length)):
        if shortest > length[j]:
            shortest = length[j]
    print(words[length.index(shortest)])

shortest_word(input("enter a sentence "))  