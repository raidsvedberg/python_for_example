total = 0
answer = 'y'
while answer == 'y':
    name = input('enter a name: ')
    print(name, 'was invited')
    total += 1
    answer = input('another name? (y/n) ')
print(total)
