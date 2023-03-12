import random as r

number = int(input('1) Addition \n'
      '2) Subtraction \n'
      'Enter 1 or 2: '))

def generate_one():
    number_one = r.randint(5, 20)
    number_two = r.randint(5, 20)
    user = int(input('enter sum of two numbers: '))
    answer = number_one + number_two
    return user, answer

def generate_two():
    number_one = r.randint(25, 50)
    number_two = r.randint(1, 25)
    user = int(input('subtract the second from the first: '))
    answer = number_one - number_two
    return user, answer

def check(user, answer):
    if user == answer:
        print('correct!')
    else:
        print('incorrect, the answer is', answer)

def main():
    if number == 1:
        user, answer = generate_one()
        check(user, answer)
    elif number == 2:
        user, answer = generate_two()
        check(user, answer)
    else:
        print('incorrect choice')

main()