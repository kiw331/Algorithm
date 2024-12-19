# N과 M (1) -  백트래킹 기초
from sys import stdin

n, m = map(int,stdin.readline().split())

res = []    #전체 정답
tmp = []    #순열 하나. res의 원소로 들어감
chk = [0] * (n+1)   #중복 방지


def recur(dep):
    # 순열 하나 완성
    if dep == m:
        res.append(tmp[:])  #tmp의 복사본 추가
        return
        
    for i in range(1, n+1):
        if chk[i] == 0:
            chk[i] = 1
            tmp.append(i)
            recur(dep+1)
            tmp.pop()
            chk[i] = 0
            
recur(0)

for i in res:
    print(*i)