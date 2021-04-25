
#1 Write a python program which returns a given list without duplicates.
l = [1,2,2,3,4,5]
s = set(l)
print(s)

#2 Write a python program which returns common elements of 2 lists.
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
s1 = set(l1)
s2 = set(l2)
print(s1 & s2)


#3 Write a python program which return elements which are in first list but not in second
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
s1 = set(l1)
s2 = set(l2)
print(s1-s2)

#4 Write a python program which return elements are or in first list, either in second, but not in both
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
s1 = set(l1)
s2 = set(l2)
print(s1^s2)

#5 Write a python program which return elements which are or in first, either in second, or in both
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
s1 = set(l1)
s2 = set(l2)
print(s1 | s2)

#6 Write  python function which get set and element value, and remove from set element with given value if exist
sample_set = {3,5,7,11,13}
list_of_num = [10, 11, 12, 13, 14]
for x in list_of_num:
    sample_set.add(x)
print(sample_set)


#7 Write a python python program, which return list from given set, where each element of list, is equal to cub of set element
l=[]
s={3,5,7,11,13}
for x in s:
    l.append(x**3)
print(l)
