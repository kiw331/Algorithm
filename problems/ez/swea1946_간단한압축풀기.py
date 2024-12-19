# 1946. 간단한 압축 풀기 D2


for t in range(1, int(input())+1):

    N = int(input())

    # 문자열 다 합치기
    al = ''

    for i in range(N):
        letter, num = input().split()
        num = int(num)
        al += letter * num

    print(f'#{t}')
    while len(al) >= 10:
        print(al[:10])

        al = al[10:]

    print(al)
