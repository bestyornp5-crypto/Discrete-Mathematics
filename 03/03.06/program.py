from time import perf_counter

def up_to_5():
    how_many = 0
    start = perf_counter()
    for a in range(1000000000, 5000000001):
        str_a = str(a)
        if '6' in str_a or '7' in str_a or '8' in str_a or '9' in str_a:
            continue
        list_of_digits = [int(n) for n in str_a]
        summ = sum(list_of_digits)
        if summ == 5:
            how_many += 1
            print(f'{how_many}: {a}')
    print(how_many)
    stop = perf_counter()
    print(f"It took: {stop-start:.2f}s.")