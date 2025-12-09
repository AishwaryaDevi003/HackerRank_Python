# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
l=list(map(int,input().split()))
if any(str(i)[::-1] == str(i) for i in l) and all(int(i)>0 for i in l):
    print(True)
else:
    print(False)
