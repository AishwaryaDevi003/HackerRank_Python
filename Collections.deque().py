# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
a=int(input())
r=deque()
for i in range (a):
    b=input().split()
    list(b)
    if b[0]=="append":
        r.append(b[1])
    elif b[0]=="appendleft":
        r.appendleft(b[1])
    elif b[0]=="pop":
        r.pop()
    elif b[0]=="popleft":
        r.popleft()
print(" ".join(r))
        
