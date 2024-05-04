from math import floor

k, n =  map(int, input().split())
l = [int(input()) for _ in range(k)]

m = floor(sum(l)/n) #k의 최대값

s, e = 1,m #초기 탐색범위
p = (e-s)//2 #현재 탐색값

# 최대값부터 1씩내리면서 정답구하기 --> 시간초과
for i in range(m, 0, -1):
    s = 0 #
    
    for j in range(k):
        s+= l[j]//i
        
    if s==n:
        print(i)
        break
        
    
    

    