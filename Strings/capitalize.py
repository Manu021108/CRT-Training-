'''
Problem:9

Capitalize the first and last character of a word 

Example:
input : hello world
output: HellO WorlD


'''

string = input("Enter the string")
#hello world

words = string.split()#['hello','world']
                        #   0       1
                #   word = 1
result = [] #HellO,WorlD

for word in words:
    
    #single character
    if len(word) == 1:
        result.append(word.upper())
        
    else:   ##['Hello    ','world']
                # 01234
                # output = HellO
        new_word =(
            word[0].upper()+  #W
            word[1:-1]+       #orl
            word[-1].upper()  #D   WorlD
            
        ) 
        result.append(new_word) 
        
print(" ".join(result))   

      