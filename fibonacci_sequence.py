# creating fibonacci sequence

def fib(n):
    fib_sequence = [1,1]  # These are the first 2 terms of the fibonacci sequence, will append to this iteratively to generate the rest
    while len(fib_sequence) < n: 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n-1]

# Running rosalind problem
print(fib(25))
