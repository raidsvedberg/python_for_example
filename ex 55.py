import random

number = random.randint(1, 5)
print(number)
user = int(input('enter a number: '))
if user == number:
    print('well done')
else:
    if user > number:
        print('bigger')
    else:
        print('smaller')
    user_new = int(input('another number: '))
    if user_new == number:
        print('correct')
    else:
        print('you lose')
