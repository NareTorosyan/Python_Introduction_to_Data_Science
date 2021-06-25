
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()

l=[]
for line in lines:
    clean_row = line.replace("+", "")
for i in clean_row:
    print(i)

for clean_row in file:
    with open(r'C:\Users\user\Desktop/new.csv', "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(clean_row)
new_file = open(r'C:\Users\user\Desktop/new.csv')
new_lines=new_file.readlines()

findata







