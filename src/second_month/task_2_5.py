
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()
for index, line in enumerate(lines):
    print("Line {}: {}".format(index,line.strip()))
text_data=[]
def datacleaner(list):
    for i in list:
        print(list[i].replace("+",""))

