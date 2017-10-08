nbr = int(input('Enter a number: '))

x = range(1, nbr+1)

for i in x:
    if i % nbr == 0:
        print(i)