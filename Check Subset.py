# Enter your code here. Read input from STDIN. Print output to STDOUT
def c():
    for i in a:
        if i in b:
            pass
        else:
            return False
        return True
q=int(input())
for _ in range(q):
    le=input()
    a=input().split()
    le1=input()
    b=input().split()
    if len(a)<len(b):
        s=c()
        if s:
            print("True")
        else:
            print("False")
    else:
        print("False")
