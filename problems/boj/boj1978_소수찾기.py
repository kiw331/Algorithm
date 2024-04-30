n = int(input())
l = [x for x in list(map(int,input().split())) if x>1] #1이상의 수만 입력받음

not_prime = 0

for x in l:
    
    # x//2+1 이상의 수는 x의 약수가 될 수 없음 -> x//2까지만 확인
    for i in range(2, x//2+1): 
        if x % i ==0:
            not_prime +=1
            break
        
print(n-not_prime)