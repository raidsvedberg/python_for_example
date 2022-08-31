array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
line = int(input('enter a line: '))
print(array[line])
column = int(input('enter a column in this line: '))
print(array[line][column])
answer = input('would you to edit this value?(y/n) ')
if answer == 'y':
    new_value = int(input('enter a new value: '))
    array[line][column] = new_value
print(array[line])
