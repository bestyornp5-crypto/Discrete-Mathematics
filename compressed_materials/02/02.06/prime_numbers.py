from time import perf_counter
from math import sqrt

start = perf_counter()
primes = [2, 3]

k = 6
while len(primes) < 10**6:
    a = k - 1
    b = k + 1
    current_sqrt = int(sqrt(b)) + 1

    for current in [a, b]:
        is_prime = True
        for p in primes:
            if p > current_sqrt:
                break
            if current % p == 0:
                is_prime = False
                break
        if is_prime:
            print(current)
            primes.append(current)
    k += 6

print(primes[:100])
print(primes[-10:])

stop = perf_counter()
print(f"It took: {stop-start:.2f}s.")
# 100 000 primes: 436.68s. -> 3.12s, the last: 1299709
# 1 000 000 primes: 92.23s. -> 72.04s, the last: 15 485 863