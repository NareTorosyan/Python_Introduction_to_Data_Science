#1 Write a Python program to multiply all the items in a list.
l = [1, 2, 3, 4, 5, 6, 7]
product = 1
for x in l:
    product = product * x
    print(product)

#2 Write a Python program to get the largest number from a list.
l = [3,8,2,9]
max_number = 0
for x in l:
    if x > max_number:
          max_number = x
    print(x)


#3Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
l=[]
for x in range(1,31):
    l.append(x**2)
print(l[5:])

# 4Write a Python program to remove duplicates from a list
l1 = [1,2,2,3,4,5,6,3]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)

#5 Write a Python program to find the most appeared element in a list.
l = [1, 2, 2, 3, 3, 3, 4, 5, 6, 3, 3]
count = 0
for x in l:
    freq = l.count(x)
    if (freq > count):
        count = freq

print(x)
