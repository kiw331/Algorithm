#1984. 중간 평균값 구하기 D2

for t in range(1, int(input())+1):

    lst = [i for i in map(int, input().split())]

    lst.pop(lst.index(max(lst)))
    lst.pop(lst.index(min(lst)))

    res = round(sum(lst)/8)

    print(f'#{t}',res)
    
    