
# 1행에서 00, 10, 01 위치에 놓는 케이스
x, l, r = 1, 1, 1

for i in range(2, int(input())+1):
    # i행에서 00, 10, 01 위치에 놓는 케이스 (다중할당으로 tmp변수 필요없음)
    x, l, r = x+l+r, x+l, x+r
    
print((x+l+r)%9901)