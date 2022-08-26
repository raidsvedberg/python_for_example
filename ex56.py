import random

number = random.randint(1, 10)
print(number)
user = int(input('enter a number: '))
while user != number:
    user = int(input('enter a number: '))
print('ok')