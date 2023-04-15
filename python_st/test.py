import sys

a,b,c,d = map(int, input().split())
print(min([a,b,abs(c-a),abs(d-b)]))
        
        
    