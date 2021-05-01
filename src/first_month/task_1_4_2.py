#1 Write a python program, which adds a new value with the given key in dict.
d = {"A":5,"B":9,"C":25}
def new_value(b):
    d["A"] = b
    return d
print(new_value(10))


#2 Write a python program which concat 2 dicts.

s1 = {"A":5,"B":9,"C":25}
s2 = {"D":19,"E":25,"F":34}
def concat(d1,d2):
    d1.update(d2)
    return d1
print(concat(s1,s2))

# 3  Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of
d = {}
values = []
keys = []


def cubes(N):
    for x in range(1, N):
        values.append(x ** 3)
    for x in range(1, N):
        keys.append(x)
    for i in range(0, len(keys)):
        d[keys[i]] = values[i]
    return d


print(cubes(10))

#4 Write a python program which create dict from 2 lists with the same length
dic = {}
l1 = [1,2,5,6,7]
l2 = ["A","B","C","D","E"]
def new_dic(l1,l2):
    for i in range(0,len(l1)):
        dic[l1[i]] = l2[i]
    return dic
print(new_dic(l1,l2))

#5 Write a python program which gets the maximum and minimum values of a dictionary.

dic = {"A":10,"B":9,"C":3}
l = list(dic.values())
def max_min(d):
    l.sort()
    return l[-1],l[0]
print(max_min(dic))



#6 Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.
d1 = {"A":5,"B":9,"C":25}
d2 = {"A":19,"E":10,"F":34}
def sum(d1,d2):
    for key,value in d2.items():
        if key in d1.keys():
            value = value + d1[key]
            d1[key]=value
    d1[key]=value
    return d1
print(sum(d1,d2))


 #7 Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string
d = {}
l = ["A","B","C","D","E","E","E"]
def new_dic(l):
    for i in range(0,len(l)):
        d[l[i]]=l.count(l[i])
    return d
print(new_dic(l))










