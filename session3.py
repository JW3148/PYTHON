# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:52:26 2016

@author: Jiahe Wang
"""

"""
The for loop
"""
list_of_numbers=[1,7,1,-5]
print list_of_numbers

for number in list_of_numbers:
    print (number*4)

list_of_numbers=[1,2,3,4,5,6,7,8,9]
sum_numbers=0
even_numbers=[]
sum_even_numbers=0

for number in list_of_numbers:
    sum_numbers=sum_numbers+number
    if number%2==0:
        even_numbers.append(number)
        sum_even_numbers=sum_even_numbers+number

print(sum_numbers)
print(sum_even_numbers)
print(even_numbers)

"""
Case you want to postion or index
Using an extra variable
"""
list_of_numbers =[1,2,3,4,5]
position=0
for number in list_of_numbers:
    print("Value at index {0:d} is {1:d}".format(position,number))
    position=position+1
    
"""
Using range() and len()
"""
list_of_numbers =[1,2,3,4,5]
for i in range(len(list_of_numbers)):
    print("Value at index {0:d} is {1:d}".format(i,list_of_numbers[i]))

"""
Using enumerate()
"""   
list_of_numbers =[1,2,3,4,5]
for i, number in enumerate(list_of_numbers):
    print("Value at index {0:d} is {1:d}".format(i,number))
    
    
"""
Example:Fibonacci Numbers
"""
fibonacci_numbers=[0,1]
for i in range(15):
    fibonacci_numbers.append(fibonacci_numbers[-1]+fibonacci_numbers[-2])

print(fibonacci_numbers)
len(fibonacci_numbers)

"""
Iterating Through Dictionaries
## Dictionary is unordered, unlike list
"""
mccs ={'Snowmobile Dealers':5598,
       'Aquariums':7998,
       'Drinking Places':5813,
       'Typewriter Stores':5978}

for key in mccs:
    print key, mccs[key]
    
"""
Partial Loops: break and continue
"""
for i in range(1,21):
    if i % 5 ==0 and i%3==0:
        break
print(i)

for i in range(20):
    if i % 5 !=0:
        continue  #means skip
    print(i)
    
"""
Comprehensions
"""
list_cube=[x**3 for x in range(10)]
print(list_cube)

##long version
list_cube=[]
for x in range(10):
    list_cube.append(x**3)
print(list_cube)

list_cube_even=[x**3 for x in range(10) if x**3%2==0]
list_cube_even
list_cube_even=[x for x in range(10) if x**3%2==0]

"""
Dictionary and Set Comprehensions
"""
cube_mapping={x:x**3 for x in range(10)}
cube_mapping

set_odds={x for x in range(10) if x%2==1}
set_odds

"""
Picking and Choosing
"""
list_cube
list_cube[::2]
"""
Functions
"""

def my_first_function(name):
    print("Hello,{0}".format(name))
    
my_first_function("James")

"""
Lambda Objects
"""
weird_math_lamba = lambda x, y: x*y+x/y-x**2
weird_math_lamba(1,3)

data=[('VA',23),('FL',12),('NY',56)]
data
data.sort
data
data.sort(key=lambda item: item[1]) 
data


def f(s):
    print(s)
    s = "Only in spring, but London is great as well!"
    return s
    
s = "I am looking for a course in Paris!" 
f(s)
print(s)
s=f(s)
s
print(a)

