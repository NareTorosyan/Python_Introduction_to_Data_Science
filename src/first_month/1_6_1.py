from task_1_3_1 import gcd
class Rational:
    def __init__(self,numerator,denumerator):
        self.__numerator = numerator
        self.__denumerator = denumerator

    def __repr__(self):
            return f"{self.__numerator},{self.__denumerator}"

    def normalize(self,numerator,denumerator):
        numerator = self.__numerator//gcd(numerator,denumerator)
        denumerator =self.__denumerator//gcd(numerator,denumerator)
        if denumerator==0:
            return "Denumerator must be non-zero value"
        else:
           return Rational(numerator,denumerator)

obj1 = Rational(10,5)
print(obj1)
print(obj1.normalize(10,5))

