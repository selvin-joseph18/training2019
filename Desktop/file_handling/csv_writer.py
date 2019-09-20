import csv

with open('data.csv','r') as file1:
    csv_reader = csv.reader(file1)
    #print(csv_reader)

    with open('copy','w') as  file2:
        csv_writer = csv.writer(file2,delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)



