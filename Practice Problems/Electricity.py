#Problem statement: 

#calculate the electricity bill using the conditions:
#1.First 100 units --> 5/unit
#2.next 100 units -->7/unit
#3.Above 200 units -->10/unit

#Take the units as input 
units = int(input("Enter the units:")) #250 

if units <= 100:
    #Bill for the first 100 units 
    bill = units * 5
elif units <= 200:  
    
    #First 100 units will be 5/unit
    #next 100 units will be 7 unit 
    bill = (100 *5)  + ((units - 100) * 7)
    
else:
    #first 100 units -- 5 
    #next 100 units -- 7
    #above 200 units -- 10
    bill = (100*5) + (100*7) + ((units-200)*10)  
    
#display the whole bill 2
print("Final bill:", bill)     

'''
units = 250 
100 * 5 = 500
100 * 7 = 700

(units - 200) * 10
   250 - 200  * 10 => 500
   
   500+700+500 ==> 1700 


'''
