# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
print(*(re.sub(r'(?<= )(&&|\|\|)(?= )',
    lambda m : 'and' if m.group() == '&&' else 'or',
    input()) 
    for _ in range(int(input()))),sep='\n')
