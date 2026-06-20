'''
#Problem-2 Palindrome:Word remains same after reversing 

"Madam" ==> "madam"                 
                     Logic
                       |
                     Input a word 
                       |
                    reverse the word 
                        |
                   compare original and reversed 
                        |
                  Palindrome or not                                         
'''

original = input("Enter the string") #Madam

reversed = original[::-1] #madam

if original == reversed:
    print("Palindrome")
else:
    print("Not a palindrome")    