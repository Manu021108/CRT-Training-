'''
text ="apple banana pineapple
strawberry banana apple"
Find the frequency of the words?
output:
{'apple':2,'banana':2,'pineapple':1,strawberry:'1'}

'''
text ="apple banana pineapple strawberry banana apple"

words = text.split()

freq ={}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
             
print(freq)  

'''
#shallow copy:

'''
student = {
    "Name":"Manish",
    "RollNo":8
}   

b = student.copy()  
print(b)  

student["RollNo"] = 9 
print(student)

print(b)

c = student 
print(c)

student["RollNo"] = 10
print(c)

#Why dict is faster?

#Hashing -- dict stores data in hashtable
#Time complexity: O(1)
# searching --> O(1)
# insert,deleting -->O(1)

data = {
    "a":1,
    "a":2
}
print(data)

'''
Create a  dict with employee 
details 
now add branch and phone num at a time 
fetch all the key and values using loop
make sure to copy before deleting any pair 
pop the last added pair 
print the pairs before deleting 

addon: make the employee a nested dict 
with multiple employees
now print key values using looping 

Problem-2:
Group anagram:
input:["eat","tea","tan"
,"ate","nat","bat"]

output:[[eat,tea,ate],[tan,nat],[bat]]

words = ["eat","tea","tan,"ate","nat","bat"]

groups = {[aet:eat,tea,ate],[ant:tan,nat],[abt:bat]}

for word in words:      #bat -> abt
    key = "".join(sorted(word))
    
    if key in groups:
        groups[key].append(word)
        
    else:
    #creates a list 
        group[key] = [word]    
        
print(list(groups.values()))        


Problem:
Top k frequent elements 
input[1,1,1,2,2,3]
k = 2
output [1,2]


nums = [1,1,1,2,2,3]
k = 2
freq = {}
for i in nums:
   if i in freq:
     freq[i] +=1
     
   else:
     freq[i] = 1
     
#sort by the frequency descending 
result = sorted(freq, key=freq.get,
      reverse = True)   
      
print(result[:k])          


'''