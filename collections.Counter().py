# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
l=list(map(int,input().split()))
n=int(input())
d=0
for i in range(n):
    a,b=map(int,input().split())
    if a in l:
        d+=b
        l.remove(a)
print(d)
        
    
    
