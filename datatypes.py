'''
Edit this file to complete the exercises in
'Efficiently Storing and Accessing Data'
'''
#!pip install fibo in IPYTHON 

#####################################################
#Some setup, creating a list and dictionary to be
#used in some of the exercises:
import fibo
import demodict
fibolist = fibo.nacci(50)
print fibolist

demodict1 = demodict.generate_dict()
print demodict1



#####################################################

#####Lists!#####

#Just to get you going, here's the answer to
#the first exercise:
maybe_your_first_list = [1, 2, 3, 4, 5]

# Find the last element of fibolist:
fibolist_last =fibolist[-1]
print fibolist_last
# Find the sum of all even entries (indices 0, 2, 4,...) of fibolist:


fibolist_even_entries_sum=sum(item for item in fibolist if item%2==0)

def divis_by_2(num):
    return num % 2 == 0
fibolist_even_entries_sum= sum(filter(divis_by_2,fibolist))
print fibolist_even_entries_sum

# Lists can be extended. The next fibonacci number is 20365011074, add it to fibolist.
fibolist.append(fibolist[-1]+fibolist[-2])
print (fibolist[-1])
print fibolist


# Can you put a reversed copy of fibolist into fibolist_reversed without changing fibolist in place?


fibolist_reverse=fibolist[:]
fibolist_reverse.reverse()

print fibolist_reverse
print fibolist



A = [1, 2, 3, 4, 5]
B = ["a", "b", "c", "d", "e"]
# Two lists can be concatenated with +. Concatenate A and B together, and store the result in A_and_B.
A_and_B = A+B
print A_and_B

# Check if 1337 is in fibolist. If it is, make is_1337_fibo True, otherwise make it False.
is_1337_fibo = 1377 in fibolist
print is_1337_fibo


#####Tuples!#####

# Here's the first answer to the tuple section:
maybe_your_first_tuple = (0, 1, 2, 3, "hello", 4, 5, 6, 7, 8, 9, 10, 1, 4, 1, 1, 91)

# Tuples also support slicing like lists. Find the even- and odd-indexed entries of your tuple:
your_first_tuple_evens = maybe_your_first_tuple[1::2]


your_first_tuple_odds = maybe_your_first_tuple[0::2]


#####Sets!#####

#Again, the first exercise is done for you.
maybe_your_first_set = set([1,2,3,4,2])
#Note that len(maybe_your_first_set) = 4, whereas if it was a list its
#length would be 5. 

# Sets are often used to find the distinct elements of a list. Find the distinct elements below:
some_repeats = [1,1,1,1,1,1,2,2,2,2,3,4,5,6,7,8,2345,345,2,52,243,5,2,345,523,45,5,4,2,2,3,5,234,2345]
distinct_elements = list(set(some_repeats))
print distinct_elements


set_A = set(range(100))
set_B = set(range(0,200,2))

# Apply the union and intersection operations to set_A and set_B as indicated:
A_union_B = set_A | set_B


A_intersection_B = set_A & set_B


#####Dictionaries!#####

#Check out all the stuff you can put in dictionaries:
maybe_your_first_dict = {'key1':'val1', 'key2': 'val2', 
                         'key3': 0, 'key4': [1,2,3], (1,2):'tuples can be keys',
                         'but not lists': ["how", "sad", "for", "lists"]}

demodict1["hello there"]="hello there value"
print demodict1

# Dictionary elements are accessed by key rather than position.
# Try it here - get the value of key "hello there" in the dictionary demodict1 (created at the top of this script):
hello_there_value = demodict1["hello there"]


# remove the key "there" from demodict1:
del demodict1["there"]
print demodict1
