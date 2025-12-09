# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b=input().split(" ")
l=list(permutations(a,int(b)))
for i in range(len(l)):
    print("".join(l[i]))
    
