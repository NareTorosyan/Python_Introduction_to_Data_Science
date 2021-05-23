class RoomException(Exception):
    def __init__(self, message, value):
        self.__message = message
        self.__value = value


    def print_obj(self):
        print(self.__message, self.__value)

class Room:
    def __init__(self, variety, count):
        try:
            if type(count) != int:
               raise RoomException("Must be integer",count)
            if count<=0:
               raise RoomException("Count must be positive ",count)
            else:
                self.__type = variety
                self.__count = count
        except RoomException as error:
            error.print_obj()


    def __repr__(self):
        return f"{self.__type},{self.__count}"

    def get_type(self):
       return self.__type

    def get_count(self):
        return self.__count

    def reserve(self,count):
        try:
            if count>self.__count:
                raise RoomException("We have no available count of these rooms",count)
            else:
                self.__count=self.__count-count
        except RoomException as error:
            error.print_obj()

    def checkout(self, count):
        self.__count = self.__count + count


class Hotel:
    def __init__(self, name, rooms):
        self.__name = name
        self.__rating = 0
        self.__rate_count = 0
        self.__rooms = rooms

    def __repr__(self):
        return f"{self.__name},{self.__rooms}"


    def get_rating(self):
        return self.__rating

    def get_name(self):
        return self.__name

    def get_rooms(self):
        return self.__rooms

    def get_rate_count(self):
        return self.__rate_count

    def rate(self,rating):
        try:
            if type(rating) != int:
                raise RoomException("Rating must be integer", rating)
            if rating>5:
               raise RoomException("Rating must be smaller or equal to 5",rating)
            if rating<0:
                raise RoomException("Rating must be positive",rating)
            else:
                self.__rate_count=self.__rate_count+1
                self.__rating=(self.__rating+rating)/self.__rate_count
        except RoomException as error:
            error.print_obj()

    def add(self, room: Room):
        try:
            if type(room) != Room:
                raise RoomException("Rating must be integer", room)
            else:
                self.__rooms.append(room)
        except RoomException as error:
            error.print_obj()

    def remove(self, room: Room):
        try:
            if type(room) != Room:
                raise RoomException("Rating must be integer", room)
            else:
                self.__rooms.pop(room)
        except RoomException as error:
            error.print_obj()

    def reserve(self, variety, count):
        for i in self.__rooms:
            if i.get_type()==variety:
                i.reserve(count)

    def checkout(self, variety, count):
        for i in self.__rooms:
            if i.get_type() == variety:
                i.checkout(count)

obj1=Room("penthouse",8)
print(obj1.get_type())
print(obj1.get_count())
print(obj1.reserve(5))
print(obj1.checkout(1))

obj2=Hotel("Golden_Palace",[Room("penthouse",3),Room("single",10),Room("double",15)])
print(obj2.get_rating())
print(obj2.get_rooms())
print(obj2.rate(4))
print(obj2.reserve("single",7))
print(obj2.add(Room("penthouse",2)))





























