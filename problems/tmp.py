
import time
import random

s = time.time()  # 시작 시간 기록

for _ in range(10**7):

    res = 100
    tmp = random.uniform(0, 200)

    # if tmp > res:
    #     res = tmp
        
    res = max(res, tmp)


e = time.time()  # 종료 시간 기록`


print(e-s, 's')