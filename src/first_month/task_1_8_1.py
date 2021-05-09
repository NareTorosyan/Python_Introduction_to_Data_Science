class MoneyException(Exception):
    def __init__(self,message,amount):
        self.__message=message
        self.__amount=amount


    def print_obj(self):
        print(self.__message,self.__amount)
n= - 100
try:
    if n < 0:
        raise MoneyException("Negative Value",n)
except MoneyException as me:
    me.print_obj()

