n = int(input())
l = list(map(int, input().split()))

m = max(l)

res = 0
for i in range(n):
    res += l[i]/m*100

res = res/n
print(res)