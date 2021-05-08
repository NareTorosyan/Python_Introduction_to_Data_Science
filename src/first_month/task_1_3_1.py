
# 1 Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.
def divider(a ,b):
    if b % a== 0:
        return True
    else:
        return False





def palindrome(number):
    if s == s[::-1]:
        return True
    else:
        return False


# 3 Write a Python function, which gets a number, and return True if that number is prime, otherwise False.

def prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            return True


# 4Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.

def perfect(number):
    l = []
    for x in range(1, number):
        if number % x == 0:
            l.append(x)
    if number == sum(l):
        return True
    else:
        return False


# 5Write a function, which gets 2 numbers, and return their Great common divisor - https://en.wikipedia.org/wiki/Euclidean_algorithm
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
