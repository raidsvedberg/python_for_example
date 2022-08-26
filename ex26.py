line = input('enter a word: ')
if line[0] in ('a', 'e', 'i', 'o', 'u'):
    print(line + 'way')
else:
    print(line[1::] + line[0] + 'ay')
