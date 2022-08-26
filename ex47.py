number1 = int(input('enter a number 1: '))
number2 = int(input('enter a number 2: '))
sum = number1 + number2
answer = input('another number? (y/n) ')
while answer == 'y':
    number = int(input('enter a number: '))
    sum += number
    answer = input('another number? (y/n) ')
print('the sum is', sum)
