number = int(input('enter a number: '))
while number < 10 or number > 20:
    if number < 10:
        print(number, 'too low')
        number = int(input('enter a number: '))
    elif number > 20:
        print(number, 'too high')
        number = int(input('enter a number: '))
print('thank you')
