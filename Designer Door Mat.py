n, m = map(int, input().split()) #accepts the input


char = ".|."
welcome = "WELCOME"
count = 1              # a counter for ".|."

def insert_char(num): #a function to return char num times
    return char*num
    
#create a nxm grid
for a in range(n):      #run the loop n times
    if n // 2 == a:     #checks if this is the middle line
        print(welcome.center(m, "-"))   #if middle, prints welcome with padding
    else:
        
        print(insert_char(count).center(m, "-"))    #calls the insert_char() like 1, 3, 5, 3, 1 times 
        if (n//2-1) > a:
            count += 2
        elif n//2 < a:
            count -= 2
        else:
            pass
