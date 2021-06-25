import datetime
from datetime import datetime
from dateutil import parser
import pandas as pd
#Write a Pandas program to create
#a) Datetime object for Jan 15 2012.
print(datetime(2012, 1, 15))
#b) Specific date and time of 9:20 pm.
print(datetime(2012, 1, 15, 21,20))
#c) Local date and time.
print(datetime.now())
#d) A date without time.
print(datetime.date(datetime(2012, 5, 22)))
#e) Current date.
print(datetime.now().date())
#f) Time from a datetime.
print(datetime.time(datetime(2012, 1, 15, 17, 20)))
#g) Current local time
print(datetime.now().time())

#2Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates.
today=datetime(2021,6,29)
tomorrow=today+pd.Timedelta(days=1)
yesterday=today-pd.Timedelta(days=1)
print(tomorrow)
print(yesterday)
print(tomorrow-yesterday)

#3Write a Pandas program to create a date from a given year, month, day and another date from a given string format.
date1=datetime.date(datetime(2021,8,21))
date2=parser.parse("07 of August,2021")
print(date1)
print(date2)

#4Write a Pandas program to create a date range using a startpoint date and a number of periods.
range=pd.date_range("2021-08-07",periods=20)
print(range)

#5Write a Pandas program to create a time series using three months frequency.
time_series=pd.date_range("31/12/20",periods=12,freq="3M")
print(time_series)
