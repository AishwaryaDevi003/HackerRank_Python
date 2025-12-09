# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
l=set(map(int,input().split()))
n1=int(input())
l1=set(map(int,input().split()))
print(len(l.difference(l1)))
