'''
string = "t m m z u x t"
          0 1 2 3 4 5 6
              L       R
Window length           
[t] = 1
[tm]= 2
[tmm] == m is duplicate Move L
still duplicate 
[m] = 1
[mz] = 2
[mzu] = 3
[mzux] = 4
[mzuxt] = 5

print(len) = 5

'''
#solution 
s = input()
left = 0
seen = set()
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        left +=1
    seen.add(s[right])  
    max_len =max(max_len,right-left+1) 
print(max_len)     