import time
start = time.time()  # 시작 시간 저장
from sys import stdin


l = [6,10,13,9,8,1]
n = 6
t = [0, l[0],l[0]+l[1]]+ [0 for _ in range(n-3)]  # t[i] = i잔 까지 고려한  최대값, 

print(t)


        

 
print("실행시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간