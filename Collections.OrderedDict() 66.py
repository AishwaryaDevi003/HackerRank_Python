# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
r={}
for i in range(n):
    x=input().split()
    item = ' '.join(x[:-1])
    p = int(x[-1])
    if item in r:
        r[item]+=p
    else:
        r[item]=p
for i,j in r.items():
    print(i,j)
