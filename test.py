import csv
import random

filename = "./data/world-cities.csv"

fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
 
for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')

print("TESTING")
randRow = rows[random.randint(0, len(rows))]

print(randRow[0], "," , randRow[1])

