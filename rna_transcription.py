def to_rna(word):
    RNA=""
    x=['A','C','G','T']
    
    nucleotides = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    for letter in word:
        if(letter not in x):
            return""
        else:
            RNA+=nucleotides[letter]
    return RNA

print to_rna("ACGTGGTCTTAA")
    		 

