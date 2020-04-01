'''Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes'''

N,k=map(int,input().split())
numbers=list(map(int,input().strip().split()))[:N]
count=0
for x in range(0,N-1):
    if(numbers[x]==k):
        count+=1
if(count>=1):
    print("yes")
else:
    print("no")


