def productivity_report(activities):
    #dict to store employee task counts 
    count = {}
    #traverse each activity
    for activity in activities:
        #John:Login --> name = John
        #task = Login
        name, task = activity.split()
        name = name.lower()
        
        #check if employee 
        # already exists in dict
        if name in count:
            count[name] +=1
        else:
            #add a new employee with count 1 
            count[name] = 1 
        
    employees = list(count.items()) 
    
    #sort alphabetically by name 
    def sort_by_name(item):
        #(John,2) -->tuple format 
        #   0  1
        return item[0]  
    employees.sort(key =sort_by_name )  
    
    #sort by task count 
    def sort_by_count(item):
        return item[1]
              
    employees.sort(key=sort_by_count,reverse = True) 
    
#input section 
n = int(input())
#list to store activities 
activites =[]
for i in range(n):
    activity = input()
    
    activites.append(activity)
productivity_report(activites)                     