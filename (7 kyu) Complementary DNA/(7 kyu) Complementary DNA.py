def DNA_strand(dna):
    # code here
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    complementDNA = ''.join([pairs[x] for x in dna])
    
    return complementDNA
