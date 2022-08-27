food = {1: input('enter a food: '), 2: input('enter a food: '),
        3: input('enter a food: '), 4: input('enter a food: ')}
print(food)
delete = input('what to delete? ')
print({key: val for key, val in food.items() if val != delete})
