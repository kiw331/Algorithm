from sys import stdin
import sys

def fact(x):
    o = x  
    while (x>1):
        x-=1
        o = o*x
    return o
    
n, k = map(int, stdin.readline().split())

if k==0 or k==n:
    sys.exit(print(1))

a = 1
for i in range(n, n-k, -1):
    a = a * i
    
res = a // fact(k)

print(res % 10007)




# import math
# print(math.factorial(a))
