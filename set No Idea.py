# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
s=list(map(int,input().strip().split()))
a=set(map(int,input().strip().split()))
b=set(map(int,input().strip().split()))
t=0
for i in s:
    if i in a:
        t+=1
    elif i in b:
        t-=1
print(t)
    
