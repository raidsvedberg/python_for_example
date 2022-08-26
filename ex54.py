import random

value = random.choice(['h', 't'])
answer = input('what a value? (h/t) ')
if answer == value:
    print('you win, this is', value)
else:
    print('you lose, this is', value)
