t = int(input())

for i in range(t):
    res, p = 0, 0   #케이스별 결과, res에 다음 더해지는 숫자
    cur = input()
    
    for j in cur:
        if j == 'O':
            p+=1
        else: 
            p=0
        res += p
    print(res)
    
# 입력전에 출력되도 정답 처리됨.