'''Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes'''



A,B,C=map(int,input().split())
if(A>B and A>C):
    X=A
    if(X**2 == B**2+C**2):
        print("yes")
    else:
        print("no")
elif(B>C and B>A):
    Y=B
    if(Y**2==A**2+C**2):
        print("yes")
    else:
        print("no")
else:
    Z=C
    if(Z**2==B**2+A**2):
        print("yes")
    else:
        print("no")

