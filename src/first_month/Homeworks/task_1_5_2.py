class MoneyException(Exception):
    def __init__(self, message, amount):
        self.__message = message
        self.__amount = amount

    def print_obj(self):
        print(self.__message, self.__amount)


class Money:
    def __init__(self, am, currency):
        try:
            if type(am) != int:
                raise MoneyException("Must be integer", am)
            if type(currency) != str:
                raise MoneyException("Must be string", currency)
            if am < 0:
                raise MoneyException("Negative Value", am)
            else:
                self.__amount = am
                self.__currency = currency
        except MoneyException as me:
            me.print_obj()

    def __repr__(self):
        return f"{self.__amount},{self.__currency}"

    def __add__(self, obj3):
        sum = self.__amount + obj3.__amount
        cur = self.__currency
        return Money(sum, cur)

    def __sub__(self, obj4):
        sub = self.__amount - obj4.__amount
        cur = self.__currency
        if sub < 0:
            return "amount can't be negative number"
        else:
            return Money(sub, cur)

    def get_amount(self):
        return self.__amount

    def set_amount(self, other):
        try:
            if type(other) != int:
                raise MoneyException("Must be integer", other)
            if other < 0:
                raise MoneyException("Negative Value", other)
            else:
                self.__amount = other
        except MoneyException as me:
            me.print_obj()

    def get_currency(self):
        return self.__currency

    def set_currency(self, other):
        try:
            if type(other) != str:
                raise MoneyException("Must be string", other)
            else:
                self.__currency = other
        except MoneyException as me:
            me.print_obj()


obj1 = Money(-100, "USD")
obj2 = Money(20, "USD")
obj3 = obj1 + obj2
obj4 = obj1 - obj2
me.print_obj3()
me.print_obj4()