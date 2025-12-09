# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=set(map(int,input().split()))
a=int(input())
for i in range(a):
    x,z=input().split()
    l1=list(map(int,input().split()))
    if x == "intersection_update":
        l.intersection_update(l1)
    elif x == "update":
        l.update(l1)
    elif x == "symmetric_difference_update":
        l.symmetric_difference_update(l1)
    elif x=="difference_update":
        l.difference_update(l1)
print(sum(l))
        
        
    
        
    
