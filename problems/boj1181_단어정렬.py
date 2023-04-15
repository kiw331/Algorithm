n = int(input())
l = list(set([ input() for _ in range(n)])) # 중복단어제거, (정렬함수 쓰려고)다시 리스트로 바꿔줌

l.sort(key=lambda x : (len(x),x))   # # 길이, 사전순으로 정렬, 키에 변수가 그대로 들어가면 사전 순

print(*l, sep='\n')