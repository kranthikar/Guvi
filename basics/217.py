'''Given numbers A,B find A^B.
Input Size : 1 <= A <= 5 <= B <= 50
Sample Testcase :
INPUT
3 4
OUTPUT
81'''

A,B=input().split()
A,B=[int(A),int(B)]
c=A**B
print(c)
