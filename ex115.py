import csv

file = open("books.csv", "r")
reader = csv.reader(file)
count = 0
for row in reader:
    print(count+1, row)
    count += 1
if count == 0:
    print("no search rows")
file.close()
