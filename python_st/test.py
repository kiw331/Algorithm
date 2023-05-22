from sys import stdin
n = int(stdin.readline())

for _ in range(n):
    l = int(stdin.readline())
    t = stdin.readline()
    
    s = set()
    for i in range(l-1):
        s.add(t[i:i+2])
        
    print(len(s))
        
    
        
        
    