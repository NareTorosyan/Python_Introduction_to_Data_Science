import pandas as pd
import numpy as np

#1Write a Pandas program to add, subtract, multiple and divide two Pandas Series
def add_sub_mul_div(s1,s2):
    return s1+s2,s1-s2,s1*s2,s1/s2


#2Write a Pandas program to convert a dictionary to a Pandas series.
def dic_to_series(dic):
    return pd.Series(dic)


#3Write a Pandas program to convert a NumPy array to a Pandas series
def np_array_to_series(arr):
    return pd.Series(arr)

#4Write a Pandas program to convert the first column of a DataFrame as a Series
def first_col_to_df(dataframe):
    return pd.Series(dataframe.iloc[:,0])


def main():
    series1=pd.Series([1,11,3,4,5,6])
    series2 = pd.Series([2,4,6,8,10,12])
    sales_data ={"client1":100,"client2":200,"client3":700,"client4":500,"client5":900}
    client_data=np.array(["client1","client2","client3","client4","clinet5"])
    other_data = {"Sales":[100,200,700,500,900],"Feedback": [5,5,4,3,5],"Crosssale": ["Yes","Yes","No","Yes","Yes"]}
    other_data_dataframe =pd.DataFrame(other_data)
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    exam_data_dataframe=pd.DataFrame(exam_data,index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    print(add_sub_mul_div(series1,series2))
    print(dic_to_series(sales_data))
    print(np_array_to_series(client_data))
    print(first_col_to_df(other_data_dataframe))
main()
