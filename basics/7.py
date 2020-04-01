'''Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
Sample Testcase :
INPUT
3
2 6
OUTPUT
yes'''

N=int(input())
L,R=input().split()
L,R=[int(L),int(R)]
if(N>L and N<R):
	print("yes")
else:
	print("no")
