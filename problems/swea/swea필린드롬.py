# 19003. 팰린드롬 문제 D3
# 미완. 들어오는 문자열 자체도 필린드롬 맞는지 알아야함
from itertools import permutations


for t in range(1, int(input())+1):

    n, m = map(int, input().split())

    lst = []
    for i in range(n):
        lst.append(input())

    res = m

    for i in range(n, 1, -1):   #1개 순열 길이는 어짜피 m

        # 순열 만들고 확인 되면 break
        for j in permutations(lst,i):
            tmp = ''.join(j)

            if tmp == tmp[::-1]:
                res = m*n
                break


    print(f'#{t}', res)