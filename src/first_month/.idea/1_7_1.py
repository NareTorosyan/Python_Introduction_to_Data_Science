
class Person:
    def __init__(self,name,surname,age,gender):
        self.name=name
        self.surname=surname
        self.age=age
        self.gender=gender


    def __repr__(self):
        return f"{self.__name},{self.__surname},{self.__age},{self.__gender}"
obj = Person("Nare","Torosyan",26,"female")
print(obj)
