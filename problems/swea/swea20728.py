# 20728. 공평한 분배 2 D3


for i in range(int(input())):
    n, k = map(int, input().split())

    l = list(map(int,input().split()))
    l.sort()

    s = 0
    e = k-1

    res = 10**9-1
    while e < n:
        
        # 정렬되있으니까 그냥 양쪽 인덱스끼리 빼면 최대값과 최소값의 차이임
        tmp = l[e] - l[s]
        
        if tmp < res:
            res = tmp
            
        e +=1
        s +=1

    print(f'#{i+1}',res)