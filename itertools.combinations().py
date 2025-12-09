# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a,b=input().split(" ")
a=sorted(a)
for i in range(1,int(b)+1):
    l=list(combinations(a,i))
    for i in range(len(l)):
        print("".join(l[i]))
    

