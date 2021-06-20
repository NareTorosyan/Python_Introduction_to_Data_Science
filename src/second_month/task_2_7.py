import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
X=range(1,100)
Y=range(2,101)
plt.plot(X,Y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line")
plt.show

