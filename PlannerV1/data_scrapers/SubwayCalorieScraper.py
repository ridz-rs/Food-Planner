import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        if len(line[0])!=0:
            print(line.strip('®'))