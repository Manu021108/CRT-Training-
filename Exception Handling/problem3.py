'''
A company wants to create a
file anazyler tools
The program should accept:
1.Accept filename from user
handle:
1.file not found
2.permission denied 
3.empty file
Display:
number of lines: len(file.splitlines())
number of words: len(file.split)
number of characters:len(file)

'''
class EmptyFileError(Exception):
    pass
class FileAnalyzer:
    def analyze(self,filename):
        try:
            file = open(filename)
            content = file.read()
            
            if content.strip() == "":
                raise EmptyFileError("File is empty")
            lines = len(content.splitlines())
            words = len(content.split())
            characters = len(content)
            #display the outputs 
            print("Lines:",lines)
            print("words:",words)
            print("characters:",characters)
            file.close()
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)        
        # except EmptyFileError as e:
        #     print(e)
        finally:
            print("analysis completed")    
filename = input("Enter the filename")
obj = FileAnalyzer()
obj.analyze(filename)