a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

nbr = int(input('Please enter a number: '))

for x in a:
    if x < nbr:
        b.append(x)

print(b)
