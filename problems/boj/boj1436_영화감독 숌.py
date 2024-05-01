n = int(input())

x = 665
cnt = 0 # 현재 몇번쨰 종말 숫지안지

while True:
    x +=1
    if "666" in str(x):
        cnt += 1
        if cnt == n:
            break
print(x) 