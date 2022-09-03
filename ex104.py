array = {}
for r in range(0, 4):
    name = input('enter a name: ')
    age = input('enter age: ')
    size = input('enter a shoe size: ')
    array[name] = {'age': age, 'size shoe:': size}

print(array)
name_del = input('enter a name to delete from array: ')
array.__delitem__(name_del)
print(array)
