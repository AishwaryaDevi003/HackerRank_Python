# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
aset=set(map(int,input().split()))
b=int(input())
bset=set(map(int,input().split()))
x=aset.difference(bset)
z=bset.difference(aset)
q=sorted(x.union(z))
for i in q:
    print(i)
