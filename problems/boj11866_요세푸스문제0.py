n, k = int(input()), int(input())

table = list(range(1,n+1))
res = []

p = k
for _ in range(n):  #사람 수 만큼 반복
    res.append(table[p])
    table[p] = -1   #이미 죽은? 사람은 -1로 
    
    for _ in range(3):
        p = p+1/(n-table.count(-1))
        while table[p]==-1: #다음 차례가 죽은 사람이면 노카운트
            p+=1
        
            
    
            
        
        