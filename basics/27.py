'''Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0'''

N,k=map(int,input().split())
numbers=list(map(int,input().strip().split()))[:N]
count=0
for x in range(0,N):
    if(numbers[x]==k):
        count+=1
if(count>=1):
    print(count-1)
else:
    print("-1")




