class Money:
    def __init__(self,am,currency):
        self.__amount=am
        self.__currency =currency
    def __repr__(self):
        return f"{self.__amount},{self.__currency}"
    def __sum__(self,obj3):
        sum = self.__amount+obj3.__amount
        cur = self.__currency
        return Money(sum,cur)
    def sub(self,obj3):
        sub = self.__amount-obj3.__amount
        cur = self.__currency
        if sub<0:
            return "amount can't be negative number"
        else:
           return Money(sum,cur)
obj1 = Money(100, "USD")
obj2 = Money(20, "USD")
obj3 = obj1.sum(obj2)
obj4 = obj2.sub(obj1)
print(obj3)
print(obj4)


