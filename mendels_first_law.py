'''
Given 3 positive integers k, m, n which represents a population
containing a number of individuals of k + m + n.
k individuals are homozygous dominant
m individuals are heterozygous dominant
n individuals are homozygous recessive
Return the probability of two random individuals producing an offspring
that contains a dominant allele.

To solve this problem, need to first determine what is the chance
of choosing a specific individual randomly.

Let population =  p
k/p
m/p
n/p
represents the chances to pick a specific genotype. 

For the second random choice, p is now p-1 (dependent probability)
with the respective value of k, m, n decreased by one according to
the first randomly picked individual.

Next need to define outcomes of breeding
Let A represent dominanant allele and a represent recessive allele
There are only 8 combinations that produce offspring with dominant allele.
Doing a mendle square for each breeding pair yields the following probabilites
to inherit a dominant allele.
AA x anything =  1
Aa x Aa = 3/4
Aa x aa = 1/2
aa x aa = 0

Then multiply each probability of rolling a pair of individuals
and the chance they create offspring with dominant allele.
Since rolling AA automatically generates dominant offspring,
these crosses are multiplied by 1.
k/p * (k-1) / (p-1) +
k/p * m / (p-1) +
k/p * n / (p-1) +
n/p * k / (p-1) +
m/p * k / (p-1)

which, after simplification, will yield this formula:
(k^2 - k + k*m + 2*n*k + m*k) / (p^2 - p)

The other combination that will yield is any containing Aa
m/p * (m-1)/(p-1)  => q * (3/4)
m/p * n/(p-1) => r * (1/2)
n/p * m/(p-1) => s * (1/2) 
which simplies to
((m^2 - m) / (2 *(p^2 - p))) + ((2 * m * n) / (4 * (p^2 - p))

Total probability for producing a dominant offspring is
p + q + r + s

Now for pseudo code for solving this problem.
define function(integers k, m, n):
    #calculate population size
    pop = k + m + n
    
    # Multiply the random pick probabilities by probabilities of
    # inheriting a dominant allele
    # Any pair containing AA
    homo_dominant_cross = ((k**2 - k + k*m + 2*n*k + m*k) / (pop**2 - pop)) * 1
    # Any pair containing Aa (excluding AA)
    hetero_dominant_cross = 
    (((m**2 - m) *3) / ((pop**2 - pop) * 4)) + ((2*m*n) / (2 * (pop**2 - pop))
    return homo_dominant_cross + hetero_dominant_cross
    
'''

def find_mendels_first_law(k, m, n):
    pop_size = k + m + n
    homo_dominant_cross = ((k**2 - k + k*m + 2*n*k + m*k) / (pop_size**2 - pop_size)) * 1
    hetero_dominant_cross = (((m**2 - m) * 3) / ((pop_size**2 - pop_size) * 4)) + ((2*m*n) / ((pop_size**2 - pop_size) * 2))
    return homo_dominant_cross + hetero_dominant_cross

# Testing function

print(find_mendels_first_law(21, 27, 22))