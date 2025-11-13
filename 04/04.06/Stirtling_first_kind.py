from time import perf_counter
from functools import cache


# [n, k] = (n-1)*[n-1, k] + [n-1, k-1]
@cache
def stirling1(n, k):
    if n == k:
        return 1
    if k == 0 or k > n:
        return 0
    return (n-1)*stirling1(n-1, k) + stirling1(n-1, k-1)


print(stirling1(5, 3))
start = perf_counter()
print(stirling1(500, 300))
stop = perf_counter()
print(f"Trwało to: {stop-start:.2f}s.")