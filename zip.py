# zip([iterable, ...])

# This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.

# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.


# Enter your code here. Read input from STDIN. Print output to STDOUT
students, subject = map(int, input().split())
X=[]
for _ in range(subject):
     X.append(list(map(float, input().split())))
scores = zip(*X)
for i in scores:
    print(sum(i)/subject)
