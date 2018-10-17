import csv
f =  open('jurnal.csv',"r")
csvreader= csv.reader(f)
id = []
date = []
for row in csvreader:
    id.append(str(row[0]))
    date.append(str(row[1]))
print(date)
