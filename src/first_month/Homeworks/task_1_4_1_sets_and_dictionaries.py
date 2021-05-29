
#1 Write a python program which returns a given list without duplicates.
def remove_duplicates(l):
    s = set(l)
    return s


#2 Write a python program which returns common elements of 2 lists.
def common_element(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 & s2


#3 Write a python program which return elements which are in first list but not in second
def dif(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 - s2


#4 Write a python program which return elements are or in first list, either in second, but not in both
def merge(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1^s2


#5 Write a python program which return elements which are or in first, either in second, or in both
def total(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1 | s2


#6 Write  python function which get set and element value, and remove from set element with given value if exist
def remove(s,a):
    if a in s:
        s.remove(a)
        return s


#7 Write a python  program, which return list from given set, where each element of list, is equal to cub of set element
def cub(s):
    list = []
    for x in s:
        list.append(x**3)
    return list


def main():
    l1 = [1, 2, 3, 3, 3, 4, 5]
    l2 = [0, 2, 7, 9, 9, 4, 5]
    sample_set = {3, 5, 7, 11, 13}
    print(remove_duplicates(l1))
    print(common_element(l1, l2))
    print(dif(l1, l2))
    print(merge(l1, l2))
    print(total(l1, l2))
    print(remove(sample_set,11))
    print(cub(sample_set))
main()