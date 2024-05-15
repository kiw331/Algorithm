n = int(input())

l = []

for i in range(n):
    s = input()
    tmp = []
    tmp.extend([s[:4], s[4:6], s[6:]])
    
    l.append(tmp)
    
m31 = (1,3,5,7,8,10,12)

for i in range(n):
    print(f'#{i+1}', end = ' ')

    int_data = list(map(int, l[i]))
    
    #월 범위
    if int_data[1] > 12 or int_data[1] < 1:
        print(-1)
        continue
    
    # 일 범위
    if int_data[2] > 30 or int_data[2] < 1:
        print(-1)
        continue
    
    # 31일
    if int_data[2] == 31 and int_data[2] not in m31:
        print(-1)
        continue
    
    # 2월
    if int_data[1] == 2 and int_data[2] > 28:
        print(-1)
        continue
    
    print(*l[i], sep='/')
    
    
        