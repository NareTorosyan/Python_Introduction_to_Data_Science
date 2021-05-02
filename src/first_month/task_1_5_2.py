class Money:
    my_class_variable = "Money"
    def __init__(self,a,b):
        self.a=a
        self.b =b
obj1 = Money(100, "USD")
obj2 = Money(20, "USD")

print((str(obj1.a))+ " " +(str(obj1.b)))
print((str(obj1.a+obj2.a))+ " " +(str(obj1.b)))
print((str(obj1.a-obj2.a))+ " " +(str(obj1.b)))


