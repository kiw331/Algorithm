# 1983. 조교의 성적 매기기 D2
import math

for t in range(1, int(input())+1):
    
    n, k = map(int, input().split())
    
    res = 0
    grade = ('A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0')
    
    # 학생들 점수 입력받으면서 환산 점수 구하기
    sd = []
    for i in range(n):
        a,b,c = map(int, input().split())
        con = a*35 + b*45 + c*20 #환산 점수
        sd.append(con)
        
    kg = sd[k-1] #찾는 학생의 환산 점수 (k'번째'니까 -1해야됨)
    
    # 정렬하고 몇등인지 찾기(제약 사항에 의해 중복값은 없음)
    sd.sort(reverse=True)
    kidx = sd.index(kg) + 1
    kidx = math.ceil(kidx / (n // 10)) # 10등일 때 등수
    res = grade[kidx-1]
    
    print(f'#{t}',res)