# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
l=[]
x={}
for i in range(a):
    s=input()
    l.append(s)
for i in range (a):
    if l[i] in x:
        x[l[i]]+=1
    else:
        x[l[i]]=1
print(len(x))
for i,j in x.items():
    print(j, end=" ")       
     
        
    
