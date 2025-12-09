# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(map(int, input().split()))
for i in range(int(input())):
    c = input().split()
    if c[0] == 'pop':
        s_list = list(s)
        s_list.pop(0)
        s = set(s_list)
    elif c[0] == 'remove':
        s.remove(int(c[1]))
    else:
        s.discard(int(c[1]))
print(sum(s))
