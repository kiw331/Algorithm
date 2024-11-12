#swea21425. += (D2)

for t in range(int(input())):
    
    a, b, n = map(int, input().split())
    
    if a > b:
        high = a
        low = b
    else:
        high = b
        low = a
    
    res = 0
    
    # 작은 수에 큰 수를 더해야 다다음 합이 더 크게 나옴
    while 1:
        high = max(high, low)
        if high > n:
            break
        
        tmp = high
        high = high + low
        low = tmp
        
        res +=1
    
    print(res)

        
            
            
            
        
    
    
    
    
