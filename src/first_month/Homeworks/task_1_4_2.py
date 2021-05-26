#1 Write a python program, which adds a new value with the given key in dict.
dic = {"A":5,"B":9,"C":25}
def new_value(key,value,d):
    d[key] = value
    return d


#2 Write a python program which concat 2 dicts.
def concat(d1,d2):
    d1.update(d2)
    return d1


# 3  Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of
def cubes(N):
    d = {}
    for x in range(1, N):
        d[x]=x ** 3
    return d


#4 Write a python program which create dict from 2 lists with the same length
def new_dic(l1,l2):
    dic = {}
    for i in range(0,len(l1)):
        dic[l1[i]] = l2[i]
    return dic


#5 Write a python program which gets the maximum and minimum values of a dictionary.
def max_min(d):
    l = list(d.values())
    l.sort()
    return l[-1],l[0]


#6 Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.
def sum(d1,d2):
    for key,value in d2.items():
        if key in d1.keys():
            value = value + d1[key]
            d1[key]=value
    d1[key]=value
    return d1


 #7 Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string
def new_dic(s):
    d = {}
    for i in range(0,len(s)):
        d[s[i]]=s.count(s[i])
    return d


def main():
    s1 = {"A": 5, "B": 9, "C": 25}
    s2 = {"D": 5, "E": 10, "F": 25}
    l1 = [1, 2, 5, 6, 7]
    l2 = ["A", "B", "C", "D", "E"]
print(new_value("A", 8, dic))
print(concat(s1,s2))
print(cubes(10))
print(new_dic(l1,l2))
print(max_min(s1))
print(sum(s1,s2))
print(new_dic("letter"))






