t = int(input())
n, s = [], []
for i in range(t):
    a, b = input().split()
    n.append(int(a))
    s.append(tuple(b))

for i in range(t):
    for j in s[i]:
        print(n[i]*j,end="")
    print()