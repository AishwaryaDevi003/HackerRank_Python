# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
for i in range(x):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except Exception as error:
        print(f"Error Code: {error}")

