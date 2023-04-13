for i in range(t):
    h, w, n = map(int,input().split())   # h, w, n
    a, b = math.ceil(n/h), n % h    #몫 -> ~호, 나머지-> 층 / 0~h까지는 1호니까 천장함수 사용
    print(str(b) +str(a).zfill(2))