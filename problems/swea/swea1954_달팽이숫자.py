from sys import stdin

a= int(stdin.readline())
l  = [int(input()) for _ in range(a)]


#방향-오른쪽, 아래, 왼쪽, 위(배열안에 있어서 x,y 반대임)
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

def next_dir(didx):
    didx = (didx+1) % 4 #원형큐 처럼 3번째인덱스 다음 0번째로
    return didx, dir[didx][0], dir[didx][1]

def printres(n):
    
    # 이차원리스트-좌표
    arr = [[-1]*n for _ in range(n)]
    
    #현재 좌표
    x,y = 0,0
    
    #현재 방향(오른쪽-0, [x+0][y+1])
    didx, dx, dy = 0, 0, 1
    
    for i in range(1, n**2+1):
        arr[x][y] = i
        
        #print("(x,y) 값: ", x, y, i)
        
        # 범위를 넘어가거나, 이미 값이 채워져있으면 방향전환
        if max(x+dx,y+dy) >= n or arr[x+dx][y+dy] != -1:            
            didx, dx, dy = next_dir(didx)
            
            #print("방향전환", didx)

            
        x, y = x+dx, y+dy
    
    for i in range(n):
        print(*arr[i])
            
        
        
for i in range(a):
    print(f'#{i+1}')
    printres(l[i])
    

