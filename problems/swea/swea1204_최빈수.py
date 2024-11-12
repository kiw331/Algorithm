# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2

for t in range(1,int(input())+1):
    
    tn = input() #쓸모없음
    lst = list(map(int, input().split()))
    res = 0
    count = [0] * 101
    
    for i in lst:
        count[i] += 1
                
        # 가장 큰수의 마지막 인덱스
        res = len(count) - count[::-1].index(max(count)) -1
        
    print(f'#{t}',res)

    
    
    
    
    