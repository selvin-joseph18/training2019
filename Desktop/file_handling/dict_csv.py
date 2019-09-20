import csv

with open('data.csv','r') as file1:
    csv_reader = csv.DictReader(file1)
    for line in csv_reader:
        print(line['Designed by'])