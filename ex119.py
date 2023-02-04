import random as r

def choise():
    min_num = int(input('enter minimum number: '))
    max_num = int(input('enter maximum number: '))
    comp_num = r.randint(min_num, max_num)
    return comp_num

def ask():
    choise_num = int(input("I'm thinking of a number... "))
    return choise_num

def check(number, number_user):
    try_again = True
    while try_again == True:
        if number == number_user:
            print('you win')
            try_again = False
        elif number_user < number:
            number_user = int(input('a bit higher '))
        else:
            number_user = int(input('a bit lower '))

def main():
    number = choise()
    number_user = ask()
    check(number, number_user)

main()

