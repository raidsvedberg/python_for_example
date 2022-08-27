password1 = input('enter a password: ')
password2 = input('enter a password again: ')
if password1 == password2:
    print('ok')
elif password1.islower() == password2.islower():
    print('they must be in the same case')
else:
    print('incorrect')
