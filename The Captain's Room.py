k = int(input())
rooms=list(map(int,input().split()))
list_sum = sum(rooms)
rooms=set(rooms)
set_sum=sum(rooms)
rooms_sum=(list_sum-set_sum)/(k-1)
A = set_sum-rooms_sum
print(int(A))
