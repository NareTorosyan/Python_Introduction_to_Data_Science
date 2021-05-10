class RationalException(Exception):
    def __init__(self, message, value):
        self.__message = message
        self.__value = value

    def print_obj(self):
        print(self.__message, self.__value)
class Rational:
    def __init__(self,numerator,denumerator):
        try:
            if type(numerator)!=int:
               raise RationalException("Must be integer",numerator)
            if type(denumerator) != int:
               raise RationalException("Must be integer", denumerator)
            if denumerator<=0:
               raise RationalException("Denumenator must be positive ", denumerator)
            if numerator<=0:
               raise RationalException("Numenator must be positive ", numerator)
            else:
                numerator,denumerator=self.normalize(numerator,denumerator)
                self.__numerator = numerator
                self.__denumerator = denumerator
        except RationalException as error:
            error.print_obj()

    def __repr__(self):
            return f"{self.__numerator},{self.__denumerator}"
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

    def normalize(self,numerator,denumerator):
        x = self.gcd(numerator,denumerator)
        return numerator//x, denumerator//x
obj1 = Rational(10,5)
print(obj1)