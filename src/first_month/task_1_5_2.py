class MoneyException(Exception):
    def __init__(self,message,amount):
        self.__message=message
        self.__amount=amount


    def print_obj(self):
        print(self.__message,self.__amount)

class Money:
    def __init__(self,am,currency):
        self.__amount=am
        self.__currency =currency

    n = 100
    try:
        if n < 0:
            raise MoneyException("Negative Value", n)
    except MoneyException as me:
        me.print_obj()

    def __repr__(self):
        return f"{self.__amount},{self.__currency}"
    def __add__(self,obj3):
        sum = self.__amount+obj3.__amount
        cur = self.__currency
        return Money(sum,cur)
    def __sub__(self,obj4):
        sub = self.__amount-obj4.__amount
        cur = self.__currency
        if sub<0:
            return "amount can't be negative number"
        else:
           return Money(sub,cur)
obj1 = Money(-100, "USD")
obj2 = Money(20, "USD")
obj3 = obj1+obj2
obj4 = obj1-obj2
me.print_obj3()
me.print_obj4()