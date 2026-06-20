'''
Check anagram 

input: SILENT -->LISTEN

sorted(input)

[e,i,l,n,s,t]

sorted(input2)

[e,i,l,n,s,t]



'''
str1 = input("Enter the string1:")
str2 = input("Enter the string2:")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not a anagram")    
