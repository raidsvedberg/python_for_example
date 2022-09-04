answer = int(input('1) Create a new file\n2) Display the file\n3) Add a new item to the file\n'
      'Make a selection 1, 2 or 3: '))
if answer not in (1, 2, 3):
    print('not in the list')
else:
    if answer == 1:
        file = open('Subject.txt', 'w')
        subj = input('enter a subject: ')
        file.write(subj + '\n')
        file.close()
    elif answer == 2:
        file = open('Subject.txt', 'r')
        print(file.read())
    else:
        file = open('Subject.txt', 'a')
        subj = input('enter new subject: ')
        file.write(subj + '\n')
        file.close()
        file = open('Subject.txt', 'r')
        print(file.read())
