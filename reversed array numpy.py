import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    r=list(reversed(arr))
    return numpy.array(r,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
