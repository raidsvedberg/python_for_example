total = 0
for r in range(0, 5):
    number = int(input('enter a number: '))
    answer = input('add? y or n ')
    if answer == 'y':
        total += number
print(total)
