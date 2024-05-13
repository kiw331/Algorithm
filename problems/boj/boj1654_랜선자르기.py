from math import floor

k, n =  map(int, input().split())
l = [int(input()) for _ in range(k)]

m = floor(sum(l)/n) #k의 최대값

s, e = 1,m #초기 탐색범위
p = (e-s)//2 #현재 탐색값


while(1):   
    
    count = 0 # 랜선길이가 p일때 랜선 개수
    for j in range(k):
        count+= l[j]//p
        
    # p값이 작음
    if count >= n:
        
        if(p):
            pass
        
        s = p
        p = p + (e-s)//2
        
    # p값이 큼
    if count < n:
        e = p
        p = s + (e-s)//2



# # 최대값부터 1씩내리면서 정답구하기 --> 시간초과
# for i in range(m, 0, -1):
#     s = 0 #
    
#     for j in range(k):
#         s+= l[j]//i
        
#     if s==n:
#         print(i)
#         break
        
    
    

    