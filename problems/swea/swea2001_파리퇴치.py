# 2001. 파리 퇴치 D2


for t in range(1, int(input())+1):
    
    n, m = map(int, input().split())
    
    # 부분합 구할 리스트 
    bb = []
    for i in range(n):
        
        input_lst = list(map(int, input().split()))
        tmp = [0]
                
        for i in input_lst:
            tmp.append(tmp[-1] + i)
        
        bb.append(tmp[:]) #tmp를 직접넣으면 안되고 복사본 써야함

    res = 0

    for i in range(n-m+1):
        for j in range(1,n-m+2):
            tmp = 0
            
            # (i,j)부터 m*m 영역의 수 모두 더하기
            for k in range(m):
                tmp += (bb[i+k][j+m-1] - bb[i+k][j-1])
            
            
            res = tmp if tmp > res else res
            
    print(f'#{t}',res)
