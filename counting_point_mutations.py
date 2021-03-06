# Given two strings s and t of equal length, return the hamming distance
# (number of different bases in s and t)
# Iterate through both strings, if there is a mismatch += 1 to a counter
# Return length of counter for solution

def find_hamming_distance(s, t):
	if len(s) != len(t):
		return print("Strings must be equal length")
	count = 0
	for i in range(len(s)):
		if s[i] != t[i]:
			count += 1
	return count

# Testing functiona
a = "CTGATTCGTAGTTGATGCCCGCATCCTGCCGCTTATTCACTACCGCGCCGCCAGGTGTCTTGGCCCGGCACTGATACCAGAGGAAGGATTACCACTGAGTAGACCTCATCCACCGCACATTCTCGCCGCACCCGTCTCGACTCCTTCCTCTTTTGCCTCGTATGATCGTTGCCTTGCTTTTGACAGCGGCGACCAAACGCACTACCTCCTTGAACAAACCCCCGGCTATACGCATAGTAATAAAATTCAGGGGAGGCACTAGATGCTCCTCCAATCTTATCGAATCGGTGTGTCCAGCCGCCTCGTCCAGCGGTTTGCGATAGATGCGAGGAACCGCCTTCTAGTTTGGTCCTGGAACCGGTTTTAGATACTATAACTTATGCCCTGGTTCTTTTCGGGGAAGAGGGCGCAGTCTCTTCGTAATTATCTAGTATGGGTTTGGGCACACCGCCCATATGTGAATGGCTCATAGCTCGGTAAATGAACTAAGGATCAAAACCAGCAAGATCGTTGCCACATGGCGCGCATACGTGTGGGCTCCACAGCTGAAGCGGAATCCGCTACTTATCAATTTGACTTGAGAGTCGCTCCGCATACAAGACATTTCTCATTTTCAACGTCCGCTTTCGGTTATTCGGTGTCGTCTTCTCTTCTTCCTTCACTCTTAAGGCATCTGGGCTTCATGCCCCGCACTTAACAAGCCATAACCCATGCCTTATCCCAGATATAGTGTCTTTCTGATCTGCCGTATGCGTGTGGACTTATGCCTAACTAGTATCACCACAGTTTGAGTTAAACCGTGGTCACCAAAAGATCATCGGTACGTAGGTTGAAGTGAGTTTCAGGAGGCGTGGGAAGTTAGTAGTTAACCGATACATGGATGGGCTTCTAATGCTCAGATTAGATGAGTTAGTTCCTATTAGAAGCT"
b = "ATATGTCATAATTCGTGCATTCATACTGCTCACAATAAACGATCGCGTCGCCGGGGCTCTTGGGGTGGGTAGATATCGAGAGCATGCGTTGTCGGAGGGTCAAAGACGCGAGGCGCAGGCAGACGGGAATTAGGATGGGTACCCTGGCCTTAAGTCATAAGTCCTCCGATGTCACGCTCGTGCGTCCGGCGACAATAGACACGAGAAACGAGATGCAATGCTTGGATATGCTCGTGTTCACAAACGTCAAATGACGTAATCGACTCATCTTAATGGCTATAGAGACGGAGTATCCAGTCGTTATGACGCTCTCCATACACGGGAATCGTGCAGCTGGGTGCTAGTGTGATCCTGAACCTGGGTCTTAAAAAGATAGCGTGAGAAGTGTCTTTATTCGGCGTAGGTGCACCCCATTGTTGGTATCTATATTATTCCGGGAGAAGAATTCCGCCCATTTGTGAGGACCATCACTATCAATAGCAGGGCGAAGAATAAGAGTTTTCGAGACCCACGCCGAAGCGCGCTCGCAGGGCTGTGATCCTACTAACAACAGCAATAGGGCCATTTTCTAACTCACTGCAGGTTTGGTCCGCATATGAGGTAGTTGAGAGACTCAACGTGCCGTCCCGTTAACACAGTGTCGGAAGATCTTCCTAAGCCACTTCTGTGGCAATCAGTAGCCGCACTCGCTAATTTACGAGCAATCAACCAGCCGAGAGCGACGAGACAGCGGCATTCTTCACCGGTCTATGGCGTTGGAATTATGTTTGATTAGTATGTGCGAGGTAGGTCCTAACCCCTGTTAAAGCCCGAAGCCACGGTACGTAGGCTGAGCTGGATTTCTTACGGTAGGTTAGTTGGGTCATTAGGAGAGTCACGAGTTGGGTTTTAACACCGGTCTATGGGGAGTTATCTCGATTTGGCATCA"

print(find_hamming_distance(a, b))
