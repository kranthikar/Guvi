'''Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes'''


A,B,C=map(int,input().split())
if(A+B>C and B+C>A and C+A>B):
    print("yes")
else:
    print("no")
