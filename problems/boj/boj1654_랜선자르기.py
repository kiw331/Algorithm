from math import floor
from sys import stdin
import time

k, n =  map(int, stdin.readline().split())
l = [int(stdin.readline()) for _ in range(k)]

m = floor(sum(l)/n) #k의 최대값

s, e = 1,m+1 #초기 탐색범위
p = (e+s)//2 #현재 탐색값

# 랜선길이가 p일때 랜선개수
def getcount(p):
    print(p,"호출")
    return sum(map(lambda x: x//p, l))

    
# 이진탐색으로 최적의 p(랜선 길이) 찾기
while(1):   
    time.sleep(1)
    count = getcount(p)
    print(s,e,p,count)
    
    # 랜선이 길다. -> 아래 범위 탐색
    if count < n:
        print("길다")
        e = p
        p = (e+s)//2
        
    # 랜선이 짧다. -> 위 범위 탐색
    elif count >= n:
        # 랜선개수가 n이상 이고 길이를 1올렸는데 count가 작아지면 현재p가 최대 길이
        if getcount(p+1) < n:
            print(p)
            break
        
        # 정답이 아니면 윗범위 탐색
        print("짧다")
        s = p
        p = (e+s)//2
        
    

# # 이진탐색으로 최적의 p(랜선 길이) 찾기 =>타임 아웃(마지막에 순차탐색 섞어서 그런듯)
# while(1):   
    
#     count = getcount(p)
    
#     # 랜선이 길다. -> 아래 범위 탐색
#     if count < n:
#         e = p
#         p = s + (e-s)//2

#     # 랜선이 짧다. -> 위 범위 탐색
#     elif count > n:
#         s= p
#         p = s + (e-s)//2
        
#     # count == n 일때. -> 순차탐색으로 p의 최대값 구하기
#     else:
#         while count == n:
#             p+=1
    
#             count = 0
#             for i in range(k):
#                 count+= l[i]//p
                
#         print(p-1)
#         break            

        
        
# # 최대값부터 1씩내리면서 정답구하기 --> 시간초과
# for i in range(m, 0, -1):
#     s = 0 #
    
#     for j in range(k):
#         s+= l[j]//i
        
#     if s==n:
#         print(i)
#         break
        
    
    

    