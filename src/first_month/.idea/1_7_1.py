
class Person:
    def __init__(self,name,surname,age,gender):
        self.__name=name
        self.__surname=surname
        self.__age=age
        self.__gender=gender


    def __repr__(self):
        return f"{self.__name},{self.__surname},{self.__age},{self.__gender}"
obj = Person("Nare","Torosyan",26,"female")
print(obj)

class Student(Person):
    def __init__(self, name, surname, age, gender,university,faculty,course,middle_score):
        super().__init__(name)
        super().__init__(surname)
        super().__init__(age)
        super().__init__(gender)
        self.__university=university
        self.__faculty=faculty
        self.__course=course
        self.__middle_score=middle_score
    def __repr__(self):
        super().__repr__()
        return f"{self.__name},{self.__surname},{self.__age},{self.__gender},{self.__university},{self.__faculty},{self.__course},{self.__middle_score}"

obj1 = Student("Nare","Torosyan",26,"female","YSU","Mathematics","Algebra",4)
print(obj1)


def set_score(self, other):
    self.__amount = other
    print_obj()

def get_score(self):
    return self.__score


def set_course(self, other):
    self.__course = other
    print_obj()

def get_course(self):
    return self.__course


def set_faculty(self, other):
    self.__faculty = other
    print_obj()

def get_faculty(self):
    return self.__faculty


def get_university(self):
    return self.__university

class Teacher(Person):
    def __init__(self, name, surname, age, gender,discipline,faculty, university,experience,salary):
        super().__init__(name)
        super().__init__(surname)
        super().__init__(age)
        super().__init__(gender)
        self.__discipline=discipline
        self.__faculty = faculty
        self.__university = university
        self.__experience = experience
        self.__salary=salary
    def __repr__(self):
        super().__repr__()
        return f"{self.__name},{self.__surname},{self.__age},{self.__gender},{self.__discipline},{self.__faculty},{self.__university},{self.__experience}"

obj2 = Teacher("Nare","Torosyan",26,"female","good","Mathematics","YSU",4)
print(obj2)

