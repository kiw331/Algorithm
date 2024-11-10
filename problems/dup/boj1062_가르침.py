
import time
s = time.time()  # 시작 시간 기록

from sys import stdin, exit
from itertools import combinations as comb

n, k = map(int, stdin.readline().split())
words = []
for _ in range(n):
    w = stdin.readline().rstrip()[4:-4]  #처음4 마지막4 문자는 항상 같음
    w = set(w) - {'a','n','t','i','c'}   # antic 다섯 글자는 항상 배움
    words.append(w)
    



res = 0
if k >= 5:  #k가 5미만이면 배울 수 있는 단어는 없음.
    
    
    # 모든 집합 합하기
    all = set().union(*words)
    
    if k-5 >= len(all):
        res = n

    #가르칠 수 있는 문자 조합 lc (미리 기본 5문자 뺐으니까 조합 길이는 k-5)
    #lc = comb(all, k-5)

    else:
        # 각 조합별 가르칠 수 있는 단어 개수 구하고 최대값이면 갱신
        for c in comb(all, k-5):
            tmp = 0
            c= set(c)
            for w in words:
                if w <= c:  #단어가 현 조합의 부분집합이다 = 읽을 수 있는 단어
                    tmp +=1
            
            if tmp > res:
                res = tmp
                

print(res)

e = time.time()  # 종료 시간 기록`
print("실행시간: ",round(e-s,3),'s', sep='')