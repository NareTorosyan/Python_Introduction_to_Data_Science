
from zipfile import ZipFile
import pandas as pd

data=pd.read_csv(r'C:\Users\user\Desktop/data.csv')
k = 3
size1 = 8
for i in range(k):
    df=data[size1*i:size1*(i+1)]
    df.to_csv(f'Regions_{i+1}.csv',index=False)
df_1=pd.read_csv("Regions_1.csv")
print(df_1)