
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()
for line in lines:
    clean_row = line.replace("+", "")

with open(r'C:\Users\user\Desktop/new.csv',"a") as f:
    writer=csv.writer(f)
    new_lines = file.readlines()
for line in new_lines:
    writer.writerow(clean_row)



