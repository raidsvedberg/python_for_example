def get_data():
    num = int(input('enter a number: '))
    return num

def counter(num):
    for r in range(1, num+1):
        print(r)

def main():
    number = get_data()
    counter(number)

main()
