import random
t = int(input())
a = [tuple(map(int, input().split())) for _ in range(t)]

grad = []

for i in range(t):
    
    print(2)
    rx,ry = random.randint(1,1000),random.randint(1,1000)
    
    while (ry/rx in grad) or ((a[i][1]-ry)/(a[i][0]-rx) in grad):
        rx,ry = random.randint(1,1000),random.randint(1,1000)
    
    grad.append(ry/rx)
    
    for j in a:
        grad.append((j[1]-ry)/(j[0]-rx))
    a.append((rx,ry))
        
    print(rx, ry)
    print(*a[i])
        

print(grad)

