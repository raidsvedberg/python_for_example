numbers = [123, 548, 879, 159]
for r in numbers:
    print(r)
number = int(input('enter a number: '))
if number in numbers:
    print(numbers.index(number))
else:
    print('that is not in list')
