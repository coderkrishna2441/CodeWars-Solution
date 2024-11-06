# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have five or more letters reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more 
# than one word is present.

def spin_words(sentence):
    # Your code goes here
    words = sentence.split(" ")[:-1]
    last_word = sentence.split(" ")[-1]
    new_sentence = ""
    for word in words:
        if len(word) >= 5:
            new_sentence += word[::-1] + " "
        else:
            new_sentence += word + " "
    if len(last_word) >= 5:
        new_sentence += last_word[::-1]
    else:
        new_sentence += last_word
    return new_sentence