array = {}
for r in range(0, 4):
    name = input('enter a name: ')
    age = input('enter age: ')
    size = input('enter a shoe size: ')
    array[name] = {'age': age, 'size shoe:': size}

name_o = input('enter a name to output: ')
print(array[name_o])
