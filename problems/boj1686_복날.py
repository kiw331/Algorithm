v, m = map(int, input().split())
xs, ys = map(float, input().split())
xt, yt = map(float, input().split())
bunker = []

while 1: #엔터 한번 더처야 입력됨
    b = input().split()
    if not b:   break
    bunker.append(tuple(map(float,b)))




    

print(v,m)
print(xs, ys)
print(xt, yt)
print(bunker)

print("Yes, visiting","other holes.")