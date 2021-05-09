class MoneyException(Exception):
    def __init__(self,message,amount,currency):
        self.__message=message
        self.__amount=amount
        self.__currency =currency

    def print_obj(self):
        print(self.__message,self.__amount,self.__currency)
n= - 100
try:
    if n < 0:
        raise MoneyException("Negative Value",n,"Currency")
except MoneyException:
    MoneyException.print_obj()

