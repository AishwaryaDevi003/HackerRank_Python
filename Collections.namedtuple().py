# Enter your code here. Read input from STDIN. Print output t
from collections import namedtuple
a=int(input())
l=[]
student = namedtuple('student',input().split())
for i in range(a):
    r=input().split()
    s=student(*r)
    l.append(int(s.MARKS))
print(sum(l)/a)
