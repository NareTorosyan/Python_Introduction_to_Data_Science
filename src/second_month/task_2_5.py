
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()
def data_cleaner(list):
    for line in list:
        Clean_row=line.replace("+","")
print(data_cleaner(lines))