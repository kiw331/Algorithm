n, r, c = map(int, input().split())
l = 2**n #현재 길이

res = 0
while l>=2: # 2*2 사분면에서 위치를 찾았으면 반복 종료
    l //= 2
    if r < l: 
        if c < l: #1사분면
            pass
        else: #2사분면
            res += l**2
            c = c - l
    else:
        if c < l: # 3사분면
            res += 2* l**2
        else: # 4사분면
            res += 3 * l**2
            c = c-l
        r = r-l # 소속되는 사분면의 상대적의 위치가 되도록 바꿔줌
        


print(res)