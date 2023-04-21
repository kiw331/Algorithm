from sys import stdin, exit

n = int(stdin.readline())

if n==0 or n==1: exit(print(n))

x, res = 1, 1
while (x < n/2):
    x *= 2
    res += 1

print(res+1)


#문제 다시 읽어보니까 복제가 무조건 *2하는게 아니고 K이하의 아무수나 된다.
# -> N/2까지 전체 복제 하다가. 마지막에 남은 수 더하면된다.







# N 범위가 너무 커서 BFS로 풀기 힘들다/
# t = [[0],]
# res = 0

# check = [0 for i in range(10**12)]  #4BYTE * 10^12 = 
# while True:
#     t.append([])
    
#     for i in t[res]:
#         t[res+1].extend([i*2,i+1])  #이전 단계에서 나올 수있는 숫자에 생성, 복제 적용
        
#     res +=1
#     if n in t[res]:
#         print(res)
#         break
        
        

