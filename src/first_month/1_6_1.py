from task_1_3_1 import gcd
class Rational:
    def __init__(self,numerator,denumerator):
        if denumerator==0:
            return "Denumerator must be non-zero value"
        numerator,denumerator=self.normalize(numerator,denumerator)
        self.__numerator = numerator
        self.__denumerator = denumerator

    def __repr__(self):
            return f"{self.__numerator},{self.__denumerator}"

    def normalize(self,numerator,denumerator):
        x = gcd(numerator,denumerator)
        return numerator//x, denumerator//x
obj1 = Rational(10,5)
print(obj1)