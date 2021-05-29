from task_1_3_1_functions import gcd

#1 Write a Python function, which Implements the Euler function.
#Euler function is return a count of numbers not great than N, which are mutually simple with N.
#Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which returns a count of numbers mutually simple with given N.

def Euler(x):
    l=[]
    for i in range(1,x):
        if gcd(x,i)==1:
               l.append(i)
    return len(l)


#2Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#2Given a ticket number n, determine if it's lucky or not.

def is_lucky_ticket(x):
    x = str(x)
    if len(x)%2==0:
        n=int(len(x)/2)
        l=[]
        for i in range(len(x)):
            l.append(int(x[i]))
        if sum(l[0:n])==sum(l[n:]):
            return True
        else:
            return False
    else:
        return "Must enter right number of digits"
print(is_lucky_ticket(132))


# 3 Write a python function, which returns the sum of digits of given number N.

def digit_sum(n):
    digits = []
    string_n = str(n)
    for x in string_n:
        digits.append(int(x))
    return sum(digits)


#4The robot is standing on a rectangular grid and is currently located at the point (X0, Y0).
# The coordinates are integers. It receives N remote commands(list with n elements each of them is a command).
# Each command is one of : up, down, left, right. Upon receiving a correct command, the robot moves one unit in the
# given direction. If the robot receives an incorrect command, it simply ignores it. Where will the robot be located
# after following all the commands?

def robot(X,Y,*args):
    x=X
    y=Y
    for i in args:
        if i=="up":
            y=y+1
        if i=="down":
            y=y-1
        if i=="left":
            x=x-1
        if i == "right":
            x=x+1
    return x,y


# 4 Write a python function, which returns the sum of digits of given number N.

def digit_sum(n):
    digits = []
    string_n = str(n)
    for x in string_n:
        digits.append(int(x))
    return sum(digits)
digit_sum(12)



#5Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121.
def next_smallest_palindrome(x):
    x=x+1
    x=str(x)
    while True:
        if x == x[::-1]:
            return x
        x=int(x)+1
        x=str(x)


def main():
       print(Euler(6))
       print(is_lucky_ticket(132))
       print(digit_sum(12))
       print(robot(5,6,"left","up"))
       print(next_smallest_palindrome(119))


