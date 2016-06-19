# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 13:29:33 2016

@author: Jiahe Wang
"""



"""
filter(boolean function, list)
map(mapping function, list)
"""
x=range(10)

def divs_by_2(num):
    return num%2==0

map(divs_by_2,x)
filter(divs_by_2,x)


"""
Lambda function: Just another way to define function
"""

map(lambda num: num**2, x)
map(lambda num: num%2==0, x)
filter(lambda num:num%2==0,x)


"""
List Comprehensions
[mapping for item in list]
[item for item in list if condition]
"""
#mapping
[item**3 for item in x]
[item%2==0 for item in x]
#filter
[item for item in x if item%2==0]


[divs_by_2(item) for item in x]
[item for item in x if divs_by_2(item)]

