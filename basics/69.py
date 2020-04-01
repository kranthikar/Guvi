'''Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
Sample Testcase :
INPUT
2 5
OUTPUT
3'''

x,y=map(int,input().split())
count=0
for i in range(x,y+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            count+=1
print(count)
