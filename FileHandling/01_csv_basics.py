# https://realpython.com/python-csv/
import csv

with open("users.csv") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

print (100*('='))

with open("users.csv") as file:
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        if index == 0:
            print(f"Coloanele sunt: {row}")
        else:
            print(f"Randul[{index}] este: {row}")


