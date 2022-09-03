array = {}
for r in range(0, 4):
    name = input('enter a name: ')
    age = input('enter age: ')
    size = input('enter a shoe size: ')
    array[name] = {'age': age, 'size shoe:': size}

for n in array:
    print(n, array[n]["age"])
