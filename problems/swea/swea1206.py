# 1206. [S/W 문제해결 기본] 1일차 - View D3

for i in range(10):
    
    n = int(input())
    l = list(map(int,input().split()))

    # 조망권 존재 여부
    zo = [1] * n
    
    res = 0
    for j in range(2, n-2):
        
        # 조망권 없는게 확실한 건물
        if zo[j] == 0:  continue
            
        # 근접한 4개 건물 중 가장높은 길이보다 높아야 조망권 생김
        tmp = l[j] - max(l[j-2], l[j-1], l[j+1], l[j+2])
        
        res += max(0, tmp) #음수더해지는거 방지
        
        # 현재 건물에 조망권 있다. -> 양옆 두개 건물은 없음(반복문 빨리넘기기)
        if tmp >= 0:
            zo[j+1], zo[j+2] = 0, 0
            
    print(f'#{i+1}',res)
        
        
    
    
    