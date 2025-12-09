# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
z=int(input())
l=[]
for i in range(z):
    x=set(map(int,input().split()))
    if a.issuperset(x):
        l.append(True)
    else:
        l.append(False)
if False in l:
    print(False)
else:
    print(True)
