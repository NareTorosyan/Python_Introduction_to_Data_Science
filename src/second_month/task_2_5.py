
import pandas as pd

data=pd.read_csv(r'C:\Users\user\Desktop/data.csv')
def data_cleaner(data):
    data = data.replace("        ", "")
    data = data.replace("+", "")
    data = data.replace("-", "")
    data = data.replace("\t ", "")
    data =data.replace("|","")

print(data.head(10))