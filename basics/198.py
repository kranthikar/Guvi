'''Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes'''


A,B,C=map(int,input().split())
if(A==B or B==C or C==A):
    print("no")
else:
    if (A + B > C and B + C > A and C + A > B):
        print("yes")
    else:
        print("no")
