import numpy as np

# [1, 3, 2, 2, 2, 4, 4] -- incorrect
# [3, 3, 2, 2, 4, 2, 4] -- correct
# [1, 1, 1, 1, 1, 1, 1]  => [5, 5, 5, 5, 5, 5, 5]
# [0, 0, 0, 0, 0, 0, 0]  => [4, 4, 4, 4, 4, 4, 4]
# 0000000 -> 4444444
# 0000000, 0000001, 0000002, 0000003, 0000004, 0000010 -> 4444444
# 129 = 1*100 + 2*10 + 9*1
# 4444444 = 4*5**6 + 4*5**5 + 4*5**4 + 4*5**3 + 4*5**2 + 4*5**1 + 4*5**0
last = 4*5**6 + 4*5**5 + 4*5**4 + 4*5**3 + 4*5**2 + 4*5**1 + 4*5**0
accepted = 0
for i in range(last+1):
    number_as_5 = np.base_repr(i, 5)  # 1004
    number_as_5 = number_as_5.zfill(7)  # 0001004
    set_of_digits = set(number_as_5)
    if len(set_of_digits) == 3:
        accepted += 1
print(accepted)