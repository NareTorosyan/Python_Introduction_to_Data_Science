
import pandas as pd
import csv
file = open(r'C:\Users\user\Desktop/data.csv')
lines=file.readlines()
for index, line in enumerate(lines):
    print("Line {}: {}".format(index,line.strip()))
def data_cleaner(list):
    for i in range(0,len(list)):
     line=list[i]
     line=list.replace("+","")
print(data_cleaner(lines))

