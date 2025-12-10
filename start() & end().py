import re 
S = input() 
k = input()

find_match = list(re.finditer(rf"(?=({k}))", S))

if find_match: 
    for i in find_match: 
        print ((i.start(1), i.end(1)-1))

else: 
    print((-1, -1))
