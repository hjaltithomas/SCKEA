import csv
import keahelp
import numpy as np
data =  open('jurnal1.csv',encoding='utf-8')
csv_data= csv.reader(data)
data_lines = list(csv_data)

#for row in data_lines[:len(data_lines)]:
    #print(row)
id = []
date = []
amount =[]
accounts_set = set()
accounts =[]
debit_credit = []
for row in data_lines:
    id.append(row[0])
    date.append(row[1])
    amount.append(row[7])
    accounts_set.add(row[5])
    debit_credit.append(row[4])
for x in accounts_set:
    accounts.append(x)
print(accounts)
