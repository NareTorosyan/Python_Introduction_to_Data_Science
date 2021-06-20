
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()
for line in lines:
    clean_row = line.replace("+", "")

for clean_row in file:
    with open(r'C:\Users\user\Desktop/new.csv', "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(clean_row)







