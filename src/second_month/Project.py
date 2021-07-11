#!/usr/bin/env python
# coding: utf-8

# In[28]:


#importing libraries
import sys
get_ipython().system('{sys.executable} -m pip install googletrans')
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from googletrans import Translator

#read the file and convert to dataframe
df = pd.read_csv(r'C:\Users\user\Desktop/Data Project 2.csv',thousands=".")
df.number.replace(0,np.nan,inplace=True)
df1=df.dropna()
print(df1)

#group the number of fires by months
df2 = df1.groupby("month")["number"].mean().reset_index()
average_number_by_month = pd.DataFrame(df2.groupby("month").mean()["number"])
average_number_by_month.plot(kind = "bar", figsize = (20,10))
plt.show()
df['English'] = df['month'].apply(Translator.translate, src='pt', dest='en').apply(getattr, args=('text',))
df


# In[ ]:

























# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




