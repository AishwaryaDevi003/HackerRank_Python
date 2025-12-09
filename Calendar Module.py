# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m,d,y=input().split(" ")
dw=calendar.weekday(int(y),int(m),int(d))
dw=calendar.day_name[dw]
print(dw.upper())
