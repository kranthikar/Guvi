'''Check whether the given 4 points form a square or not.
Example:
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes'''


import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
a = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
b = math.sqrt( (x3 - x2)**2 + (y3 - y2)**2 )
c = math.sqrt( (x4 - x3)**2 + (y4 - y3)**2 )
d = math.sqrt( (x1 - x4)**2 + (y1 - y4)**2 )
e = math.sqrt( (x3 - x1)**2 + (y3 - y1)**2 )
f = math.sqrt( (x4 - x2)**2 + (y4 - y2)**2 )

if(a==b==c==d and e==f):
    print("yes")
else:
    print("no")
