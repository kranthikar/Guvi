'''Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes'''

import math
N,M=input().split()
N,M=[int(N),int(M)]
a=M*N
b=math.sqrt(a)
if(b-math.floor(b)==0):
    print("yes")
else:
    print("no")



