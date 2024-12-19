# 2005. 파스칼의 삼각형 D2



for t in range(1, int(input())+1):
    
    
    N = int(input())
    print(f'#{t}')


    print(1)
    pre = [0,1,0]
    
    # i는 현재 출력되는 숫자 수
    for i in range(2, N+1):
        cur = []
        
        # 현재 수열 한줄 만들고 출력
        for j in range(i):
            cur.append(pre[j] + pre[j+1])
        print(*cur, sep=' ')
        
        #양쪽에 0붙이고 다음순서로
        pre = [0] + cur[:] + [0]
        
        
    
    
    
    
    
    
    