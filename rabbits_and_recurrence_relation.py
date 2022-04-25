# Given integers n and k, return the total number of rabbits after n months, 
# if each reproduction age rabbit pair produces litter of k rabbit pairs

def rabbit_count(n, k):
    fib_sequence = [1,1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]*k)
    return fib_sequence[n-1]

# Test function
rabbit_count(29, 3)