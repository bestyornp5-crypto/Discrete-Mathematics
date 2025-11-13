from itertools import product

accepted = 0

for shuflle in product([1, 2, 3, 4, 5], repeat=9):
    if len(set(shuflle)) == 3:
        accepted += 1

print(accepted)

# Ball1 -> Cell3
# Ball2 -> Cell4
# Ball3 -> Cell5
# Ball4 -> Cell3
# Ball5 -> Cell5
# Ball6 -> Cell3
# Ball7 -> Cell4