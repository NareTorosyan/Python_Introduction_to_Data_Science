
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
        super().__init__(name,surname,age,gender)
        self.__university=university
        self.__faculty=faculty
        self.__course=course
        self.__middle_score=middle_score

    def __repr__(self):
        return super().__repr__()+" "+f"{self.__university},{self.__faculty},{self.__course},{self.__middle_score}"



    def set_university(self, university):
        self.__university = other

    def get_university(self):
        return self.__university


    def set_faculty(self, other):
         self.__faculty = other

    def get_faculty(self):
        return self.__faculty

    def set_course(self, other):
         self.__course = other

    def get_course(self):
         return self.__course


    def semiddle_score(self, other):
        self.__middle_score = other

    def get_middle_score(self):
        return self.__middle_score



class Teacher(Person):
    def __init__(self, name, surname, age, gender,university,faculty,discipline,experience,salary):
        super().__init__(name,surname,age,gender)
        self.__university=university
        self.__faculty=faculty
        self.__discipline=discipline
        self.__experience=experience
        self.__salary = salary

    def __repr__(self):
        return super().__repr__()+" "+f"{self.__university},{self.__faculty},{self.__discipline},{self.__experience},{self.__salary}"

    def set_university(self, other):
        self.__university = other

    def get_university(self):
        return self.__university


    def set_faculty(self, other):
         self.__faculty = other

    def get_faculty(self):
        return self.__faculty

    def set_discipline(self, other):
        self.__discipline = other

    def get_discipline(self):
        return self.__discipline


    def set_experience(self, other):
         self.__experience = other

    def get_experience(self):
         return self.__experience

    def set_salary(self, other):
         self.__salary = other

    def get_salary(self):
        return self.__salary



obj1 = Student("Nare","Torosyan",26,"female","YSU","Mathematics","Algebra",4)
obj2 = Teacher("Nare","Torosyan",26,"female","YSU","Mathematics","good",10, 400000)
print(obj1)
print(obj2)

