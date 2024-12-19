# 뱀 G4
# 미해결

#boj3190_뱀 G4
from collections import deque

N = int(input())    #보드
K = int(input())    #사과 개수

apple = []  #사과좌표
for i in range(K):
    r, c = map(int, input().split())
    apple.append((r, c))

L = int(input())
turn = deque()
for i in range(L):
    t, c = input().split()  #c: L이 왼쪽으로 90도, D가 오른쪽으로 90도
    turn.append((int(r), c))

#보드 초기화
board = [[0]*(N+1) for _ in range(N+1)]

#사과 위치 마킹
for a in apple:
    board[a[1]][a[0]] = 1

#뱀 위치
loc = deque()
loc.append([1,1])

#뱀 머리 위치
head = [1,1]

#방향: 동남서북
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

#현재 방향
cd = 0

#정답 - 이동 횟수
res = 0

print(apple)
print(turn)

def turnDL(cd):

    #오른쪽 회전
    if turn[0][1] == 'D':
        return (cd+1)%4

    # 왼쪽회전 0 -> -1 -> 3
    if turn[0][1] == 'L':
        return  (cd-1) if cd!=0 else 3

while 1:
    res +=1

    #머리위치 이동(주의: board는 두번째 원소가 x좌표임)
    head[0] += dy[cd]
    head[1] += dx[cd]

    #작성 편하게 임시변수만들기
    x, y = head

    # 범위 넘어가거나 몸통 만나거나
    if x > N or x<1 or y > N or y<1 or head in loc:
        print("게임끝")
        break

    #머리가 사과만나면 사과 지우기
    if board[x][y] == 1:
        print("사과")
        board[x][y] = 0

    #아니면 위치 조정
    else:
        loc.popleft()


    # 머리 추가(범위 확인↑을 먼져해야됨)
    loc.append([x,y])


    # 방향 전환 이벤트가 남아있고
    if turn:
        # 방향 전환하는 시간이 되면
        if res == turn[0][0]:

            # 방향 바꾸고 방향 턴 원소 빼기
            cd = turnDL(cd)
            turn.popleft()


print(res)

