array = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
         "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anna": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
         "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
print(array)
name, region = input('enter a name: '), input('enter a region: ')
print(array[name][region])
new_value = int(input('enter a new value: '))
array[name][region] = new_value
print(array[name])
