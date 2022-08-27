word = input('enter a word: ')
list = []
for r in word:
    list.append(r)
print('\n'.join(list[::-1]))
