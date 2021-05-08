class Money:
    def __init__(self,am,currency):
        self.__amount=am
        self.__currency =currency
    def __repr__(self):
        return f"{self.__amount},{self.__currency}"
    def __add__(self,obj3):
        sum = self.__amount+obj3.__amount
        cur = self.__currency
        return Money(sum,cur)
    def __div__(self,obj4):
        sub = self.__amount-obj4.__amount
        cur = self.__currency
        if sub<0:
            return "amount can't be negative number"
        else:
           return Money(sub,cur)
obj1 = Money(100, "USD")
obj2 = Money(20, "USD")
obj3 = obj1+obj2
obj4 = obj1-obj2
print(obj3)
print(obj4)