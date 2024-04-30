# n번째 피보나치 수
n = int(input())

f = [0 for _ in range(100)]   

def fibo(n):
    if f[n]!= 0:    return f[n]
    
    if n==1 or n==2:   
        f[n]=1
    else: 
        f[n] = fibo(n-1)+fibo(n-2)
    return f[n]

print(fibo(n))