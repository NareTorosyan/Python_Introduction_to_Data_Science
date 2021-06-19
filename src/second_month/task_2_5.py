
import pandas as pd
import csv
with open(r'C:\Users\user\Desktop/data.csv') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

