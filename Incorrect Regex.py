import re
res="False"
pattern = r'(?:[*+?]|\{\d+(?:,\d*)?\})\+'    # ++,*+,?+,{..}+
for _ in range(int(input())):
    inp=input()
    if re.findall(pattern,inp):
        res="False"
    else:
        try:
            re.compile(inp)
            res="True"
        except re.error as e:
            res="False"
    
    print(res)
