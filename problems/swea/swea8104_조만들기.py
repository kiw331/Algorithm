# swea8104. 조 만들기 D3
# 풀었는데 파이썬이라 체점이 안되네

def recur(start, st):
    global end, K

    # 상태변수가 True 일때 그대로 넣기
    if st == True:
        for i in range(1, K+1):
            jo[i] += (start + i)
    # False이면 거꾸로
    else:
        tmp = []
        for i in range(1, K+1):
            tmp.append(start + i)

        tmp.reverse()
        tmp.insert(0, 0)
        for i in range(1, K+1):
            jo[i] += tmp[i]

    # 마지막 학생 끝
    if start + K == end:
        return

    recur(start+K, not st)


for t in range(1, int(input())+1):

    # 인원, 조
    N, K = map(int, input().split())
    end = N * K

    res = 0
    jo = [0]* (K+1)

    # 상태 변수 1일 때는 정방향으로 삽입, -1일 때는 뒤집어서
    st = True
    recur(0, st)

    print(f'#{t}',*jo[1:])