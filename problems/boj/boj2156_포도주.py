# n = int(input())
# l = [int(input()) for _ in range(n)]
n=6
l = [6,10,13,9,8,1] #33
# l = [6,10,13]
if n<3:    print(sum(l))

else:
    res = 0    
    t = [0, l[0],l[0]+l[1]] + [0 for _ in range(n-2)]  # t[i] = i잔 까지 고려한  최대값
     
    for i in range(2,n):
        print('I: ',i,'   l[i]',l[i])
        t[i+1] = max(
            t[i],                     # 이번 잔은 안 마심          16
            l[i] + t[i-1] + l[i-1],     # 이번 잔과 이전 잔을 마심 
            l[i] + t[i-2] + l[i-2]      # 이번 잔과 전전 잔을 마심 0 6 13
        )
    print(t[n])
    