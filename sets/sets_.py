'''
what is a set?

Collection of unordered unique elements 
-> Unordered
->unique (Never allows duplicates)
why?
->fast searching -->O(1)
->duplicates removal 

how to create a set?

numbers = {1,2,3,4,5}
print(numbers)




'''
#Creation of set
numbers = {1,2,3,4,5}
print(numbers)

numbers = {1,2,2,2,3,4,5}
print(numbers)

num = [1,2,3,3,4,4,5]

unique = set(num)

print(unique)

#checking the muatbility
# numbers[0] = 10

# print(numbers)

#set is unordered ---> fixed indexing (NO)

numbers.add(10)\
    
#1st way -->create 
num = {1,2,3,4,5}

#2nd way -->create 
s = set([1,2,3,4,5])

# freq = {}

#empty set - creation
s = set()
s.add(1)
print(s)

#Multiple elements:
s.update([2,3,4,5])

print(s)

#Removing the element
# s.remove()
print(s)

#discard:
print(s.discard(10))
print(s)

#pop():Deletes the random element
s.pop()

#clear():

print(20 in s)

'''
What is hashing?
Hashing will convert data into the 
unique hash values 

Python uses:
1.hash tables 
2.Hash functions
target = 10
set = {1,2,3,4,10}

unlike linear search 
hash(10)
it directly jumps to location 

search ,insert,delete --> O(1)

Set Operations:

1.Union  |
2.Intersection
3.Difference 

'''
a = {1,2,3,4}
b = {5,6,7,8}

print(a|b)
print(a.union(b))

#intersection:

print(a & b)
print(a.intersection(b))

#difference
print(a - b)
print(a.difference(b))

#symmetric difference:Elements not common
a = {1,2,3}
b = {2,3,4} #1,4

print(a ^ b)
a.symmetric_difference(b)

#subset and superset 

a = {1,2}
b = {1,2,3,4}

print(a.issubset(b))
print(b.issuperset(a))

#Frozenset: Immutable version of set 
#cannot add 
#cannot del 
#cannot update

fs = frozenset([1,2,3,4,5])

print(fs)

'''
  feature       List  tuple dictionary set   
  ordered        yes   yes     No       No
  Mutability     Yes   No      Yes      Yes 
  Allow duplicat Yes   yes    keys:no val:allow  No
  Indexing       Yes   yes    No       No
    
    
    can I store list inside the set?
    1.list
    2.dict
    3.set 
    
TasK: 
create a list with squares of numbers
Convert the list with 
squares of a number to set  
Try to repeat the squares two times 
add the multiples of 2 to the same 
set at a single time 
-->separate the set with 2 diff sets 
multiples of 2 
squares 
Now perform all the set operations on both
   
Problem:
Find the length of longest consecutive sequence 
input:[100,4,200,1,3,2]
output:[4]  1,2,3,4

  
    
    
'''

