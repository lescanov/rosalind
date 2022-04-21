#given a dna string s, return the complement of s

'''
The solution here will be to to take the negative index and save it, giving the reverse of the original dna sequence. 
Will use a dictionary to convert to the complement
'''

def reverse_complement(dna):
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reverse = dna[::-1]
    reverse_complement_sequence = ""
    for nucleotide in reverse:
        reverse_complement_sequence += complement[nucleotide]
    return print(reverse_complement_sequence)

# %%
#testing output of function
reverse_complement("CATTGGAAATATATCATCATTAGCGCCACGCTATCAGTCTAACGGATTCTTGCCCAAGTGCTGGCTACGCTTTAACGGCCGATCGGTTGGTATGCACGCACTTGTAGACGAGAACTGCACAGCTCAGGGTGCGAACACTATACCCAACCCCTGTGCTGTCAAAACAACTATACCATTATAGAATGCCTAAGTGCGATTATACGTTTAGTTTTCCGCCTTAAATCAACCGGTATAGGGTCCAGTCCCATGAACTGGCCAAAAAGTAAAAAGGGAGAGTAGCCTAAGGGTGAACCGACGACATATCAAGAAGCACACTGAATCCACGCTCCCCTCACGCGACAAGGGAATTGCTCGGACCGAACTATTTCAGCGAGATAACAGAGCCATGGAACGGGGCGGTGCTTACCTCGCATGCTTCCCTTGTCAAATGCTGGTAATGTGGTAGCTGGTGAGCAGGTCCCTAACATATAAAGCCTTTACTGTGGATAGCATTGGGTGAACAGAATCTCTTGCCGCCATGGCTTACTATAATTCCGCGATCACTTGACCGTTTTAGTGTGGCGTATGGAGAGCCCACATAGGCGCGGCAACGTAGAGTGTGTTGAAGTATTCCCGATTTAGTACAATGGGCTATGGTCACGATGCTGATGTTGGTACTTTCCCTCCATCCCCACGACAGGAGTCCTAAAATGTAGAACTTTTATAATCTTAACGCAGAGTGTTTTGTACTCATTACATATTTCCAGTTGTCATAAAGAACTCAGGATGACAGGAGCTCCAATTCCTCCATACTGGTTATTACATGTTCACCTCTTCCATACCTAAAAGGCTGCGGGTGAGGTCTAAGCACCTATCCCAATAAGGATCGATGCTCTAATGCCCTAAGGCTGCTCCAGTACACGCGTAGTCGCAAAGGTGCCTGGAAAACTAACGGAATAGCGAGTTCGACAGCG")