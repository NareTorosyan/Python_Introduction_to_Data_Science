class Room:
    def __init__(self, type, count):
        self.__type = type
        self.__count = count

    def __repr__(self):
        return f"{self.__type},{self.__count}"

    def get_type(self):
        print(self.__type)

    def get_count(self):
        print(self.__count)

    def reserve(self):
        r=5
        if r<=self.__count:
            print(self.__type,self.__count-r)
        else:
           print("We have no available rooms")


    def checkout(self):
        r=5
        print(self.__type, self.__count + r)

obj1=Room("penthouse",3)
print(obj1)
obj1.get_type()
obj1.get_count()
obj1.reserve()
obj1.checkout()

class Hotel:
    def __init__(self, name, rating,rate_count,rooms):
        self.__name = name
        self.__rating = rating
        self.__rate_count = rate_count
        self.__rooms = rooms

    def get_rating(self):
        print(self.__rating)


    def get_rooms(self):
        print(self.__rooms)



obj2=Hotel("Golden_Palace",4.8,5000,[Room("penthouse",6),Room("single",3),Room("double",15)])
obj2.get_rating()
obj2.get_rooms()
