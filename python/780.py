'''You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00'''


code
x,y,z=input().split()
x,y,z= [float(x), float(y),float(z)]
SI=(x*y*z)/100
a=round(SI,2)
print(a)
