'''Print "Odd" or "Even" for the corresponding cases.

Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

Input Description:
A number is provided as the input.

Output Description:
Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases. Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

Sample Input :
2
Sample Output :
Even'''



code

n=float(input())
num=round(n)
if n==0:
    print("zero")
else:
    flag=num%2
    if(flag==0):
        print("Even")
    elif(flag==1):
        print("Odd")
