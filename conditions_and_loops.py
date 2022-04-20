#given two positive integers [a,b], sum all odd integers from a to b, inclusively
def odd_sum(a, b):
    sum_of_odds = 0
    for num in range(a, b+1):
        if num % 2 == 1:
            sum_of_odds += num
    return sum_of_odds

#testing function
odd_sum(10, 20)
11+13+15+17+19

#running data from rosalind
odd_sum(4348, 8439)