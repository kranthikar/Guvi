'''Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd'''

N,M=input().split()
N,M=[int(N),int(M)]
C=N+M
if(C%2==0):
	print("even")
else:
	print("odd")

