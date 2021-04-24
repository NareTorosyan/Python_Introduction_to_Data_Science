

#1 Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.
def new_function(a,b):
    if a % b==0:
        return True
    else:
        return False
a = new_function(48,6)
print(a)

#3 Write a Python function, which gets a number, and return True if that number is prime, otherwise False.

def new_function(x):
    for i in range(2,x):
        if x%i == 0:
            return False
        else:
            return True
a = new_function(211)
print(a)