#1 Write a python program, which adds a new value with the given key in dict.
d = {"A":5,"B":9,"C":25}
d["A"] =10
print(d)

#2 Write a python program which concat 2 dicts.
d1 = {"A":5,"B":9,"C":25}
d2 = {"D":19,"E":25,"F":34}
d1.update(d2)
print(d1)

#3 Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of
d={}
N=90
values=[]
keys=[]
for x in range(1,N):
    values.append(x**3)
print(values)
for x in range(1,N):
    keys.append(x)
print(keys)
for i in range(0,len(keys)):
    d[keys[i]]=values[i]
print(d)

#4 Write a python program which create dict from 2 lists with the same length
dic = {}
l1 = [1,2,5,6,7]
l2 = ["A","B","C","D","E"]
for i in range(0,len(l1)):
    dic[l1[i]] = l2[i]
print(dic)

#5 Write a python program which gets the maximum and minimum values of a dictionary.

dic = {"A":10,"B":9,"C":3}
l = list(dic.values())
l.sort()
print(l[-1])
print(l[0])

#6 Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.
d1 = {"A":5,"B":9,"C":25}
d2 = {"A":19,"E":25,"F":34}
d3 = {}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
           d3[i] = j + y
print(d3)

# 7 Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string
d = {}
l = ["A","B","C","D","E","E","E"]
for i in range(0,len(l)):
    d[l[i]]=l.count(l[i])
print(d)










