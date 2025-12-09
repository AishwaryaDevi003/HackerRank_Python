def minion_game(string):
    v="aeiouAEIOU"
    s=0
    k=0
    for i in range(len(string)):
        if string[i] in v:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if k>s:
        print(f"Kevin {k}")
    elif s>k:
        print(f"Stuart {s}")
    else:
        print("Draw")
        
        
            
            
    # your code goes here

