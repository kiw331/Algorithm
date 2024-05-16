from itertools import combinations

n, c = map(int, input().split())
l = sorted([int(input()) for i in range(n)])

# 메모리 초과
'''n, c = map(int, input().split())
l = sorted([int(input()) for i in range(n)])

#0, n-1 제외한 설치 위치(인덱스)
arr = list(combinations(list(range(1, n-1)), c-2))


res = 0
for i in arr:
    comb = [0] + list(i) + [n-1]

    #print('comb',comb)
    
    # 공유기들 사이의 거리
    dis = 1000000000
    for j in range(c-1):
        tmp = l[comb[j+1]] - l[comb[j]] #현재 두 공유기 사이의 거리
        #print('tmp', tmp)
        
        # 현재 조합에서 최소값(가장인접한 공유기 간 거리) 찾기
        if tmp < dis:
            dis = tmp
            
    # 정답-최대값 갱신
    res = max(res, dis)
    
print(res)'''
            
        
            
        