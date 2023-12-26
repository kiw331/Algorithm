n = int(input())
l = [x for x in list(map(int,input().split())) if x>1] #1이상의 수만 입력받음

res = 0

for x in l:
    
    for i in range(1, x//2+1): # x//2+1 이상의 수는 x의 약수가 될 수 없음 -> x//2까지만 확인
        if x % i ==0:
            continue
        
    # 안쪽 반복문 통과 했으면 약수가 없다는 의미
    res += 1
    
print(res)