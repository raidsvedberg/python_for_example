import csv

def add_file():
    file = open('Salary.csv', 'a')
    name = input('enter a name: ')
    salary = int(input('enter a salary: '))
    string = name + ', ' + str(salary) + '\n'
    file.write(string)
    file.close()

def view_table():
    file = open('Salary.csv', 'r')
    for r in file:
        print(r)
    file.close()

def main():
    again = True
    while again == True:
        print('1) Add to file\n'
              '2) View all records\n'
              '3) Quit program\n'
              'Enter the number of your selection: ')
        choice = int(input('enter your choice: '))
        if choice == 1:
            add_file()
        elif choice == 2:
            view_table()
        elif choice == 3:
            again = False
        else:
            print('incorrect choice. try again: ')

main()