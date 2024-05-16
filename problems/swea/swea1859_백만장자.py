# swea1859 백만장자

t = int(input())

for i in range(t):
        
    n = int(input())
    l = list(map(int, input().split()))
    
    s = 0
    m = max(l)
    

    res = 0
    for j in range(n-1):
        if l[j] < m:
            res += (m-l[j])
            
        elif l[j] == m:
            m = max(l[j+1:])
        
    print(f'#{i+1}', res)



'''시간초과
t = int(input())

for i in range(t):
        
    n = int(input())
    l = list(map(int, input().split()))
        
    s = 0
    e = l.index(max(l))
    
    res = 0
    while True:
                        
        res += l[e]*(e-s) - sum(l[s:e])
        
        # 리스트의 마지막 까지 확인
        if e == n-1:
            break
        
        s = e+1
        e = l.index(max(l[e:]))
        if e < s:
            e += 1
        
    
    print(f'#{i+1}', res)'''