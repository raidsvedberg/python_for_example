array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
line = int(input('enter a line: '))
print(array[line])
new_value = int(input('enter a new value to add into line: '))
array[line].append(new_value)
print(array[line])
