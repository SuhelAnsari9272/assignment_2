def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

print(sieve_of_eratosthenes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
