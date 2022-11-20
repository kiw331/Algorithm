# n번째 피보나치 수

n = int(input())

def fibo(n):
    if n==1 or n==2:
        return 1
    else :
        return fibo(n-1)+fibo(n-2)
    
    
print(fibo(n))


#시간 초과


