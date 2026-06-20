'''
A company stores server logs in a file:
write a python program:
1.read log.txt
count:
total lines 
ERROR messages 
WARNING messages 
INFO messages
Display analysis report 

Log Format:
INFO server started 
ERROR database failed 
WARNING Low memory 

Report:
count ?
'''
class LogAnalyzer:
    def analyze_logs(self):
        try:
            with open("logs.txt","r") as file:
                lines = file.readlines()
                
                error_count = 0
                warning_count = 0
                info_count = 0
                for line in lines:
                    if 'ERROR' in line:
                        error_count +=1
                    elif 'WARNING' in line:
                        warning_count +=1
                    elif 'INFO' in line:
                        info_count +=1
                print("Log Report")   
                print(
                    "TotalLines:",len(lines)
                )  
                print(error_count)
                print(info_count)
                print(warning_count)
        except FileNotFoundError as e:
            print(e)
            
obj = LogAnalyzer()
obj.analyze_logs()