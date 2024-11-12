#1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3

#n은 현재 교환횟수
def dfs(n):
    global res
    
    # 마지막 교환까지 끝났을 때 최대값과 비교
    if n==c:
        res = max(res, int("".join(map(str, l))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):
            l[i], l[j] = l[j], l[i]
            
            chk = "".join(map(str, l))
            if (n,chk) not in vst:
                dfs(n+1)
                vst.append((n,chk))
            
            l[i], l[j] = l[j], l[i] #원상복구

        

for t in range(int(input())):
    
    l, c = input().split()
    c= int(c)
    l = list(map(int,l))
    L = len(l)
    
    res = 0
    
    vst = []    #중복 체크 (레벨, 숫자)
    
    dfs(0)
    
    print(f'#{t+1}', res)
    
    
    

    