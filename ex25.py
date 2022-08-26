name = input('enter a name: ')
if len(name) >= 5:
    print(name.lower())
else:
    surname = input('enter a surname: ')
    print((name + surname).upper())
