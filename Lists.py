if __name__ == '__main__':
    N = int(input())
    a=[]
    for i in range(N):
        x=input().split(" ")
        l=list(x)
        # if len(l)==3:
        #     a.l[0](int(l[1]),int(l[2]))
        #     continue
        # elif len(l)==2:
        #     a.l[0](int(l[1]))
        #     continue
        # elif l[0]=="print":
        #     print(a)
        #     continue
        # else:
        #     a.l[0]
        #     continue
        if l[0]=="insert":
            a.insert(int(l[1]),int(l[2]))
        elif l[0]=="append":
            a.append(int(l[1]))
        elif l[0]=="print":
            print(a)
        elif l[0]=="remove":
            a.remove(int(l[1]))
        elif l[0]=="append":
            a.append(int(l[1]))
        elif l[0]=="sort":
            a.sort()
        elif l[0]=="pop":
            a.pop()
        elif l[0]=="reverse":
            a.reverse()
            
