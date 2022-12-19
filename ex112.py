import csv

file = open("books.csv", "a")
name = input("enter book name: ")
author = input("enter author: ")
year = input("enter year: ")
file.write(str(name + ", " + author + ", " + year + "\n"))
file.close()
