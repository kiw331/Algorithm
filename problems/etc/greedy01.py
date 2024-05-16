'''
자연수 n, k 입력. 
n이 1이 될때 까지 k로 나누거나 -1
최소 수행 횟수 구하기
'''

n, k = map(int, input().split())

res = 0

while 1:
    
    # k로 나눠지는 수 중에 (빼기로 만들수 있는) n과 가장 가까운 수 구하기*
    t = (n // k) * k
    
    res += (n-t) 
    n = t
    
    # n을 더이상 k로 못나눌때 반복 종료
    if n < k:   break
    
    n = n//k
    res += 1
    
    
res += (n -1)
print(res)
        
    
