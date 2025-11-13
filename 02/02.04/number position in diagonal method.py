from fractions import Fraction

MAX = 100

matrix = []
for denominator in range(1, MAX+1):
    list_of_numbers = []
    for numerator in range(1, MAX+1):
        list_of_numbers.append(Fraction(numerator, denominator))
    matrix.append(list_of_numbers)


print("DIAGONAL METHOD MATRIX for n≤9:")
for row in matrix:
    if row[0].denominator >= 10:
        break
    for i, col in enumerate(row, start=1):
        if i >= 9:
            print(f"{col.numerator}/{col.denominator}")
            break
        else:
            print(f"{col.numerator}/{col.denominator}", end=', ')

printed = set()
to_see = []
for column in range(0, 8+1):
    for i in range(column+1):
        current = matrix[i][column-i]
        if current not in printed:
            printed.add(current)
            to_see.append(current)

print()
print("The consecutive numbers in the diagonal method for n≤9:")
for element in to_see:
    how_to_show = f"{element.numerator}/{element.denominator}" if element.denominator != 1 else f"{element.numerator}"
    if element is not to_see[-1]:
        print(how_to_show, end=', ')
    else:
        print(how_to_show)

text = input(f"Enter the number to check in the diagonal method in the form numerator/denominator:")
num, den = [int(x) for x in text.split('/')]
search = Fraction(num, den)

counted = set()
iterator = 0
found = False
for column in range(0, MAX*2):
    for i in range(column + 1):
        if i > MAX - 1 or column - i > MAX - 1 or column - i < 0:
            continue
        current = matrix[i][column - i]
        if current not in counted:
            iterator += 1
            counted.add(current)
            if current == search:
                found = True
                print(f"The number {text} is on the place {iterator} in the diagonal method.")
                break
    if found:
        break
else:
    print(f"Number not found in the diagonal method.")
    print(f"The number cannot be represented as a fraction with a numerator and denominator ≤ {MAX}.")
    print(f"If you want, increase the 'MAX' parameter in the program code and run the program again.")