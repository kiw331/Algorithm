# 18799. 평균의 평균 D4

from itertools import combinations


for t in range(1, int(input())+1):
    
    n = int(input())
    s = list(map(int, input().split()))
    
    
    avg1 = 0
    for i in range(1, n+1):
        combs = combinations(s, i)
        
        # i개를 조합했을 때 각 조합의 평균 구하기
        for j in combs:
            avg2 = sum(j)/i 
            avg1 += avg2 #일단 다 더하고
            
    avg1 = avg1/(2**n-1) #전체 조합수로 나워서 평균 구하기
    
    if avg1 == float(int(avg1)): # 정수형은 .0 출력 안함
        avg1 = int(avg1)
    
            
    print(f'#{t}',avg1)