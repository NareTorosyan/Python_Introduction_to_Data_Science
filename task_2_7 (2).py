#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
X=range(1,100)
Y=range(2,101)
plt.plot(X,Y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line")
plt.show


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


#2Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016
import matplotlib.pyplot as plt
import pandas as pd
data={"2016-10-03":[774.25,776.065002,769.5,772.559998],"2016-10-04":[776.030029,778.710022,772.890015,776.429993],"2016-10-05":[779.309998,782.070007,775.650024,776.469971],"2016-10-06":[779,780.47998,775.539978,776.859985
],"2016-10-07":[779.659973,779.659973,770.75,775.080017]}
df = pd.DataFrame(data)
df.plot()
plt.show()


# In[27]:


#3Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
import matplotlib.pyplot as plt
import pandas as pd
data={"2016-10-03":772.559998,"2016-10-04":776.429993,"2016-10-05":776.469971,"2016-10-06":776.859985,"2016-10-07":775.080017}
df = pd.DataFrame(data,index=["2016-10-03","2016-10-04","2016-10-05","2016-10-06","2016-10-07"])
df.plot()


# In[ ]:





# In[39]:


#4Write a Python programming to display a bar chart of the popularity of programming Languages
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors=["blue","red","orange","green","brown"]
plt.bar(languages, popularity, color=colors)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")


# In[42]:


#5Write a Python programming to create a pie chart of the popularity of programming Languages. 
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors=["blue","red","orange","green","brown"]
plt.pie(popularity,labels=languages,colors=colors,autopct='%1.1f%%')
plt.title("PopularitY of Programming Language")


# In[44]:


#6Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.
from pylab import randn
X = randn(200)
Y = randn(200)
plt.scatter(X,Y, color='b')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




