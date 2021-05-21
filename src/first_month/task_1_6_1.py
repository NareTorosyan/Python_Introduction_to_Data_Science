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
                numerator,denominator=self.normalize(numerator,denominator)
                self.__numerator = numerator
                self.__denominator = denominator
        except RationalException as error:
            error.print_obj()

    def __repr__(self):
        return f"{self.__numerator},{self.__denominator}"

    def __add__(self, obj3):
        num = (self.__numerator * obj3.__denominator)+(self.__denominator * obj3.__numerator)
        denom = self.__denominator * obj3.__denominator
        return Rational(num, denom)

    def __sub__(self, obj4):
        num = (self.__numerator * obj4.__denominator) - (self.__denominator * obj4.__numerator)
        denom = self.__denominator * obj4.__denominator
        return Rational(num, denom)

    def __mul__(self, obj5):
        num = self.__numerator * obj5.__numerator
        denom = self.__denominator * obj5.__denominator
        return Rational(num, denom)



    def __truediv__(self, obj6):
        num = self.__numerator * obj6.__denominator
        denom = self.__denominator * obj6.__numerator
        return Rational(num, denom)

    def __gt__(self, obj7):
        num1 = self.__numerator * obj7.__denominator
        num2 = self.__denominator * obj7.__numerator
        return num1>num2

    def __eq__(self, obj7):
        num1 = self.__numerator * obj7.__denominator
        num2 = self.__denominator * obj7.__numerator
        return num1==num2

    def __lt__(self, obj8):
        num1 = self.__numerator * obj8.__denominator
        num2 = self.__denominator * obj8.__numerator
        return num1<num2


    def __ge__(self, obj9):
        num1 = self.__numerator**obj9.__denominator
        num2 = self.__denominator**obj9.__denominator
        return num1>=num2


    def __le__(self, obj10):
        num1 = self.__numerator * obj10.__denominator
        num2 = self.__denominator * obj10.__numerator
        return num1<=num2


    def __pow__(self, obj11):
        num = self.__numerator ** obj11.__denominator
        denom = self.__denominator ** obj11.__numerator
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
        return self.__denominator

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


obj = Rational(30,5)
print(obj)

obj1 = Rational (3, 5)
obj1.set_denominator(10)
obj2 = Rational (4, 3)
obj3 = obj1+obj2
obj4 = obj2-obj1
obj5 = obj1*obj2
obj6 = obj2/obj1
obj11 = obj1**obj2
print(obj3)
print(obj4)
print(obj5)
print(obj6)
print(obj1>obj2)
print(obj1==obj2)
print(obj1<obj2)
print(obj1>=obj2)
print(obj1<=obj2)
print(obj1**obj2)
