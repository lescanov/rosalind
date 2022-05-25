# Given integers n and k, return the total number of rabbits after n months, 
# if each reproduction age rabbit pair produces litter of k rabbit pairs

def rabbit_count(n, k):
    fib_sequence = [1,1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]*k)
    return fib_sequence[n-1]

# Test function
rabbit_count(29, 3)

# Now creating a moral rabbit model, where rabbits live for m months, where m <= 20

def mortal_rabbit_count(n, m):
    fib_sequence = [1, 1]  
    while len(fib_sequence) < n:
        if len(fib_sequence) > m:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2] - fib_sequence[-m])  # This is incorrect
        else:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n - 1]

mortal_rabbit_count(89, 19)