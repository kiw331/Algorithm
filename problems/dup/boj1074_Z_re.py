from sys import stdin
n, r, c = map(int, stdin.readline().split())

# 한변의 길이. (r,c)가 어느 사분면에 있는지 확인하면서 길이를 반씩 줄임 
l = n**2

res = 0

while l >= 2:
    
    # 계산 편의를 위해 변이 길이를 미리 2로 나누기
    l //= 2
    
    #1사분면
    if  r < l and c < l:
        continue
        
    #2사분면
    if r < l and c >= l:
        res += l**2
    
    #3사분면(편의상 3사분면이 왼쪽아래)
    
    #4사분면
    


