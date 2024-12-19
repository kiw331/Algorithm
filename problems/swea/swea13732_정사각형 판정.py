# 13732. 정사각형 판정 D3
# 미완 -아마 bfs/dfs

for t in range(1,int(input())+1):

    n = int(input())

    lst = [input() for _ in range(n)]

    res = 'no'

    for i in range(n-1):
        for j in range(n-1):
            if lst[i][j] == '#':
                if lst[i+1][j] == '#' and lst[i][j+1]=='#' and lst[i+1][j+1] == '#':
                    res = 'yes'
                    break
        if res == 'yes':
            break

    print(f'#{t}',res)