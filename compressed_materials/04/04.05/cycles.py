from itertools import permutations

N = 5
K = 3


def permutation_to_cycles(perm):
    """The function converts a given permutation into cycles."""
    visited = [False] * len(perm)
    cycles = []

    for i in range(len(perm)):
        if not visited[i]:
            cycle = []
            current = i
            while not visited[current]:
                visited[current] = True
                cycle.append(current + 1)  # +1, because in Python indexes are 0-based
                current = perm[current] - 1
            cycles.append(tuple(cycle))
    return cycles


all_permutations = permutations(range(1, N + 1))
result = []

for p in all_permutations:
    cycles = permutation_to_cycles(p)
    if len(cycles) == K:
        result.append(cycles)

print(f"Number of {N}-element permutations having exactly {K} cycles: {len(result)}")
for i, cycles in enumerate(result, start=1):
    cycle_str = "∘".join(f"({' '.join(map(str, cyc))})" for cyc in cycles)
    print(f"{i}: {cycle_str}")
