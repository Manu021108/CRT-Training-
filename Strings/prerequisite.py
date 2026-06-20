'''
Count the frequency of the characters 

Example: 

input: aaabc
output: 
a:3
b:1
c:1

dict = {'a':10,'b':3}


'''

string = input("Enter the string:") 
                #a a b c
              #  0 1 2 3
            # ch =3
freq = {} #{a:2,b:1,c:1}

for ch in string:
    if ch in freq:
        # freq[a] = frq[a]+1
        freq[ch] +=1
    else:
        #freq[c] = 1
        freq[ch] = 1     
        
for key in freq:
    print(freq[key]) 
    # print(freq[c])  2 1 1  
    
    
'''
Find the maximum freq character?

Example:

input: aaabcd

a:3  ___> a
b:1
c:1
d:1

'''
     
string = input("Enter the string:") 
                #a a b c
              #  0 1 2 3
            # ch =3
freq = {} #{a:2,b:1,c:1}

for ch in string:
    if ch in freq:
        # freq[a] = frq[a]+1
        freq[ch] +=1
    else:
        #freq[c] = 1
        freq[ch] = 1  
        
max_freq = 0
max_char = ""           
        
for key in freq:
    if freq[key] > max_freq:
        # freq[a] > 0
        max_freq = freq[key]
        max_char = key
        
print(max_freq)        