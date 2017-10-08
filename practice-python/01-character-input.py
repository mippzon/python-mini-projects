current_year = 2017

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

born_year = current_year - age

print('{} will celebrate the 100th birthday in year {}'.format(
    name, born_year+100))
