# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# Your function receives one side of the DNA (string, except for Haskell); you need to return the 
# other complementary side. DNA strand is never empty or there is no DNA at all 
# (again, except for Haskell).

def DNA_strand(dna):
    # code here
    complementary_strand = ""
    for symbol in dna:
        if symbol == "A":
            complementary_strand += "T"
        elif symbol == "C":
            complementary_strand += "G"
        elif symbol == "T":
            complementary_strand += "A"
        elif symbol == "G":
            complementary_strand += "C"
    return complementary_strand