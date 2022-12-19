import csv

file = open("books.csv", "a")
number = int(input("how many rows append? "))
for r in range(0, number):
    name = input("enter book name: ")
    author = input("enter author: ")
    year = input("enter year: ")
    file.write(str(name + ", " + author + ", " + year + "\n"))
file.close()

file = open("books.csv", "r")
search = input("enter author for search: ")
reader = csv.reader(file)
count = 0
for row in reader:
    if search in file:
        print(row)
        count += 1
if count == 0:
    print("no search rows")
file.close()
