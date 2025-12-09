# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=input()
# for i in range(len(n)):
#     if n.isalnum and n[i] == n[i-1]:
#         print(n[i])
#         break
#     else:
#         print("-1")
import re
s=re.search(r'([0-9A-Za-z])\1+',input())
print(s.group(1) if s else -1)
        
