'''
Word Frequency ANalyzer
A company wants to analyze the text 
write a python program :
1.Read contents from data.txt
2.count the frequency of each word
3.display most repeated word
4.handle the exceptions 
'''
class WordAnlyzer:
    def analyzer(self):
        try:
            with open("new.txt","r") as file:
                content = file.read().lower()
                words = content.split()
                frequency = {}
                for word in words:
                    if word in frequency:
                        frequency[word] +=1
                    else:
                        frequency[word] = 1
                print("word Frequencies")  
                for key,value in frequency.items():
                    print(key,":",value)  
                '''
                maximum = max(frequency,key=frequency.get)
                {
                    hello:3
                    world:2
                    bye:3   
                }
                frequency= bye,hello,world
                key= frequency.get(key) = 3,2,3
                return max values 
                
                '''
                            
                maximum = max(frequency,key=frequency.get)   
                print("Most Repeated word",maximum) 
        except FileNotFoundError as e:
            print("File not found",e)
obj = WordAnlyzer()
obj.analyzer()            