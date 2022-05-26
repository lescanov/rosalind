'''
Problem:
Given 2 strings, s and t, where t is a substring of s, return all locations of t in s. 

Approach:
Need to check if length of s is greater than t and that t is contained within s.
If true, use a combination of regular expression and other functions to determine
where the indices of these matches occur.
The index expected by rosalind is 1 indexed, so will add +1 to python indices

Pseudocode:
import re
import numpy as np

define function (string, substring):
    if length(s) > length(t) and s contains t:
        iterate regex match substring across string
    
    # Convert from 0-index to 1-index
    result = np.array(match_indices)
    result = result + 1
    
    return print(result)

'''
import re
import numpy as np

# Solution taken from here: 
# https://stackoverflow.com/questions/18933711/find-all-occurrences-of-a-substring-including-overlap

def find_indices_of_motif(string, substring):
    if len(string) > len(substring) and substring in string:
        match_indices = [match.start() for match in re.finditer('(?={0})'.format(re.escape(substring)), string)]
    result = np.array(match_indices)
    result = result + 1
    return(print(result))

a = "TCGACAGTTCCGAACAGTTCCTTTTGGGACACAGTTCCCGGATACAGTTCCGTACAGATCAGTTCCGAGCAGTTCCTCAGTTCCACAGTTCCCGAACATCTCGCAGTTCCCCAGTTCCGCCCCAGTTCCGCAGTTCCGAATGTCCTCAACAGTTCCCAGTTCCCAGTTCCTCAGTTCCCAGTTCCCAGTTCCGGGAAAGCAGTTCCTCCAGTTCCCCAGTTCCGGACAGTTCCCCGCTGATGCAGTTCCCATCGGCAGTTCCCCTGGCTATATCAGTTCCCAGTTCCACAGTTCCGGTCGCAGTTCCGCCAGTTCCGCAGTTCCCAGTTCCCAGTTCCCCAGTTCCGCCAGTTCCGAAACAGTTCCTCAGTTCCTCCAGTTCCTAACAGTTCCCAGTTCCACAGTTCCTCAGTTCCCATCAGTTCCGCAGGATGGAAGGACAGTTCCCGCAGTTCCTTGATGCTCAGTTCCCAGTTCCCAGTTCCATCAATTGCCGGTATGCAGTTCCACAGTTCCACCCCAGTTCCCAATATGAGGACAGTTCCCAAGCATCCAGTTCCCAGTCAGTTCCCAGTTCCATGCTCAGTTCCCAGTTCCCAGTTCCACAGTTCCATACAGTTCCCTTCTCGACAGTTCCTTCAGTTCCCCCGTCAGTTCCCAGTTCCATTCAGTTCCACGATCAGTTCCCAACAACAGTTCCCAGTTCCTCGACGCAGTTCCGGGGCAGTTCCCAGTTCCAACAACAGTTCCTAATACCACAGCAGTTCCCTTGTCCAGTTCCCAGTTCCAGACAGTTCCAACAGTTCC"
b = "CAGTTCCCA"

find_indices_of_motif(a, b)