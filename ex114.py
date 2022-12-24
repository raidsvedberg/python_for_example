import csv

file = open("books.csv", "r")
year_i = int(input("enter initial year: "))
year_f = int(input("enter final year: "))
reader = list(csv.reader(file))
count = 0
for row in reader:
    if (int(row[2]) <= year_f and int(row[2]) >= year_i):
        print(row)
        count += 1
if count == 0:
    print("no search rows")
file.close()
