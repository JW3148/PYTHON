# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:43:28 2016

@author: Jiahe Wang
"""

a_new_list=['a','b','c']
a_new_list

empty_list=list()
empty_list=[]

my_list=[5,2,3,91]
my_list
my_list[0]
my_list[2]

x=[4,1,2,5,3,1]
x[:4]   #first 4 number
x[2:4]  #3rd to 4th
#note the upper bound is not inclusive
x[1::2]
x[::-1]

x=[1,2,3,31,24,7]
x.remove(31) #delete the first element with this value
x

del x[2] #delete the third element
x

x=[1,3,2,5,4]
x.reverse
print(x)

x.sort()
print(x)

x=[1,3,3,2]
x.append(-1)

y=["a","c","e"]

x+y

y.index("c")

print(3 in y)

print('hi!' in y)

x=[1,2,3,2]
len(x)

x.append(-1)
len(x)
sum(x)


range(5) #Starting from 0, 5 numbers
# 5 means the number of element

range(2,5) 
#stating from 2, 5 is exclusive

range(2,9,3)
#3 is te incremental

x=range(5)

range(0,5)

x=list(range(5))
x

my_list =[1,1,2,3,5,8,13]
x=my_list
x
my_list
x[2]=14
#x, mylist changes together, when we update one of them
#x, mylist are just stikers to the same object
import copy

copy_of_list =my_list[:]
my_list

copy_of_list =my_list.copy()

some_place=(37.234,-76.654)
some_place
some_place[0]
singleElement=(3.14,)

from collections import namedtuple
Place = namedtuple('Place',('lat','lon'))
#Place is a class of named tuples
p1=Place(77.234, -76.654)
#p1 is an instance of Place
print(p1)
print(Place)

print(p1.lat)

{1,2,3,4,5}
x=set([1,2,3,4,3])
print(x)
set()
print(5 in x)
print(1 in x)

x={1}
x.add(2)
print x
x.add(4)
x.remove(1)
print x

y=x.copy()
print(y)
print(x)


#dictionary
x={"key":"value"}
print(x["key"])

x=dict(key1="value1", key2="value2")
print(x)
print x["key2"]

x=dict()
print x
x["key1"]="value1"
x["key2"]="value2"
del x["key1"]

x={}
x["key1"]=1
print x
x[0]=2
x[(1,2,3)]=5
x[(1,2,3)]


#string, list, tuple, set, dic
mylist=[5,2,3,91]
print mylist
mytuple=(37.234,-76.345)  #represhent fixed size collections
print mytuple  
#tuple is immutable
myset=set([1,3,4])
print x
mydict=dict(key1='value1',key2='value2')
print mydict




