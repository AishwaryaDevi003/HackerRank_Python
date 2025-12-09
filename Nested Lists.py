if __name__ == '__main__':
    l=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        s.append(score)
    s=sorted(set(s))
    s=s[1]
    l.sort()
    for i,k in l:
        if k == s:
            print(i)
