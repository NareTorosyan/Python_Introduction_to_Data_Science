
#1Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
s = "Spring"
print(s[:2] + s[-1]+s[-2])

#2Write a Python program to remove the nth index character from a nonempty string.
s = "Spring"
n=3
s1=s[0:n]+s[n+1:]
print(s1)

#3Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
s = "Spring"
n = 5
s4 = s[-1]+s[1:n]+s[0]
print(s4)


#4Write a Python function to get a string made of 4 copies of the last two characters of a specified string
s = "Spring"
s3 = s[-2:]*4
print(s3)


#1Write a Python program that make a list from given string
s = "Spring"
n = 6
s4 = [s[0],s[n-1]]
print(s4)


#2Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.
x = [1,2,3,4,5,6,7,8]
x.pop(0)
x.pop(3)
x.pop(4)
print(x)


#3Write a Python program which add an element to the given list
x = [1,2,3,4,5,6,7,8]
x.append(3)
print(x)


#4Write a Python program which concat 2 lists.
s1 = ["winter","spring"]
s2 = ["summer", "fall"]
print(s1+s2)


