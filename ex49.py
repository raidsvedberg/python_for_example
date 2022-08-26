compnum = 50
count = 1
number = int(input('enter a number: '))
while number != compnum:
    if number < compnum:
        print(number, 'too low')
        count += 1
        number = int(input('enter a number: '))
    elif number > compnum:
        print(number, 'too high')
        count += 1
        number = int(input('enter a number: '))
print('you took', count, 'times')
