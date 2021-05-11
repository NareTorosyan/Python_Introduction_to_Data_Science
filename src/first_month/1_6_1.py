class RationalException(Exception):
    def __init__(self, message, value):
        self.__message = message
        self.__value = value

    def print_obj(self):
        print(self.__message, self.__value)
class Rational:
    def __init__(self,numerator,denominator):
        try:
            if type(numerator)!=int:
               raise RationalException("Must be integer",numerator)
            if type(denominator) != int:
               raise RationalException("Must be integer", denominator)
            if denominator<=0:
               raise RationalException("Denumenator must be positive ", denominator)
            if numerator<=0:
               raise RationalException("Numenator must be positive ", numerator)
            else:
                numerator,denumerator=self.normalize(numerator,denominator)
                self.__numerator = numerator
                self.__denominator = denominator
        except RationalException as error:
            error.print_obj()

    def __repr__(self):
        return f"{self.__numerator},{self.__denominator}"

    def __mul__(self, obj3):
        num = self.__numerator * obj3.__numerator
        denom = self.__denominator * obj3.__denominator
        return Rational(num, denom)

    def __truediv__(self, obj4):
        num = self.__numerator * obj4.__denominator
        denom = self.__denominator * obj4.__numerator
        return Rational(num, denom)


    def get_numerator(self):
        return self.__numerator

    def set_numerator(self, other):
        try:
            if type(other) != int:
                raise RationalException("Must be integer", other)
            if other<=0:
               raise RationalException("Numenator must be positive ", other)

            else:
                self.__numerator = other
        except RationalException as me:
            me.print_obj()

    def get_denominator(self):
        return self.__denumerator

    def set_denominator(self, other):
        try:
            if type(other) != int:
                raise RationalException("Must be integer", other)
            if other <= 0:
                raise RationalException("Denominator must be positive ", other)

            else:
                self.__denominator = other
        except RationalException as me:
            me.print_obj()

    @staticmethod
    def gcd(number1, number2):
        if number1 % number2 == 0:
            return number2
        if number2 % number1 == 0:
            return number1
        else:
            x = 0
            for i in range(1, number1):
                if number1 % i == 0 and number2 % i == 0:
                    x = i
            return x

    def normalize(self,numerator,denominator):
        x = self.gcd(numerator,denominator)
        return numerator//x, denominator//x
obj1 = Rational(10,5)
print(obj1)




obj1 = Rational (3, 5)
obj2 = Rational (4, 3)
obj3 = obj1 * obj2
obj4 = obj1/obj2
print(obj3)
print(obj4)