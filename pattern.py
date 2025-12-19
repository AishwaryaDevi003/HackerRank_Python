# *
# **
# ***
# ****
# *****
n=6
for i in range(n):
    print('*'*i)
    
#       *
#      ***
#     *****
#   *******
#   *********
#  ***********
# " "*(n-i-1) , '*'*(2*i+1)
for i in range(n):
    print(' '*(n-i-1),'*'*(2*i+1))
    
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end="")
    print()
    
# 1
# 23
# 456
# 78910
# 1112131415   
num=0
for i in range(1,n+1):
    for j in range(1,i):
        num+=1
        print(num,end="")
    print()
