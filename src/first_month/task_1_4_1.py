
#1 Write a python program which returns a given list without duplicates.
l=[1,2,3,3,3,4,5]
def remove_duplicates(l):
    s = set(l)
    return s
print(remove_duplicates(l))


#2 Write a python program which returns common elements of 2 lists.
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
def common_element(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 & s2
print(common_element(l1,l2))


#3 Write a python program which return elements which are in first list but not in second
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
def dif(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 - s2
print(dif(l1,l2))

#4 Write a python program which return elements are or in first list, either in second, but not in both
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
def merge(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1^s2
print(merge(l1,l2))

#5 Write a python program which return elements which are or in first, either in second, or in both
l1 = [1,2,2,3,4,5]
l2 = [1,2,5,6,7,8]
def total(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 | s2
print(total(l1,l2))

#6 Write  python function which get set and element value, and remove from set element with given value if exist
sample_set = {3,5,7,11,13}
def remove(s,a):
    for x in s:
        if a==x:
           return s.remove(x)
        else:
            return s
    return s
print(remove(sample_set,7))



#7 Write a python  program, which return list from given set, where each element of list, is equal to cub of set element

sample={3,5,7,11,13}
def cub(s):
    list = []
    for x in s:
        list.append(x**3)
    return list
print(cub(sample))
