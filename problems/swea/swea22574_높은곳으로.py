# 22574. 높은 곳으로 D3


for t in range(int(input())):
    N, P = map(int, input().split())
    
    res = 0
    
    for i in range(1, N+1):
        
        res += i
        
        if res == P:
            res-=1
            
    print(res)



# 이진수 바꾸는 부분 어려움

# # n자리 문자열 반환 빈자리 0
# def get_bin():
#     pass
    
# # 폭탄에 걸리는지 확인
# def bomb():
#     chk = 0
    
#     for i in range(1, N+1):
#         chk += ch[i-1] * i
    
#         # 폭탄에 걸리면
#         if chk == P:
#             return True
    
#     return False


# for t in range(int(input())):
    
#     N,P = map(int, input().split())
#     res = 0
    
#     # 최대값이 되는 선택지 (모두 이동하는 경우)
#     ch = '1'*N
    
#     # 최대 선택지 부터 1씩 빼면서 폭탄에 안걸리는 선택지 찾기
#     while True:
        
#         #1빼고 이진수로 바꾸면 뒤에서 부터 줄어듬. 앞에있는 1을 먼져 빼야하니까 문자열 뒤집기 필요 
#         ch = format(int(ch, 2)-1, 'b')[::-1]
        
#         # 선택 ch가 폭탄을 지나가는지 확인
#         if bomb:
#             continue
        
#         # 폭탄에 안걸리는 선택지 - 최대값
#         best_choice = ch
#         break

#     # 선택지로 부터 층수 구하기
#     for i in range(1, N+1):
#         res += best_choice[i-1] * i
    
#     print(res)
    
    
    

# # 재귀 깊이로 인한 런타임 에러

# def recur(n, floor):
#     global res
    
#     # N번째 선택이 끝났을때 최대값 갱신
#     if  n==N:
#         if floor > res:
#             res = floor
        
#         return
    
#     n +=1
    
#     # N번째 선택에서 같은 층 방문 기록이 있으면 리턴
#     if (floor+n) in vst[n]:
#         return
    
#     # 방문 체크
#     vst[n].append(floor)
        
#     #다음 선택에서 올라가지 않음
#     recur(n, floor)
    
#     #다음 선택에서 올라가는 경우(폭탄없는 층)
#     if floor+n != P:
#         recur(n, floor+n)

    
    
# for t in range(int(input())):
    
#     N,P = map(int, input().split())
#     res = 0
    
#     # ex) vst[3]: 3번째 선택에서 방문한 층 리스트
#     vst = [[0]] + [[] for _ in range(N)]
    
#     # 선택, 현재층
#     recur(0, 0)
    
#     print(res)
    