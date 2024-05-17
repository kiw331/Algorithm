# 20021. 소수 그래프 D4

from bisect import bisect_left, bisect_right

def isprime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num**1/2) + 1):
        if num  % i == 0:
            return False
        
    return True


primes = [i for i in range(1, 1001) if isprime(i)]

print(primes)

n = 6
if n in primes:
    print(-1)
    
    
# 가능한 정점수 2n+1 < h < n(n-1)/2
h = primes[bisect_left(primes, 2*n+1): bisect_right(primes, int(n*(n-1)/2))]

if not h:
    print(-1)
    
print(h)

        

# for i in range(int(input())):
    
    
    
#     print(f'#{i+1}')