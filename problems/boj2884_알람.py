import sys
import  datetime

h, m =  map(int, sys.stdin.readline().split())
setTime = datetime.timedelta(hours = h, minutes = m-45)

print(setTime.seconds//3600, setTime.seconds%3600//60 )


# #정답
# a,b=map(int,input().split())
# x=a*60+b-45
# print(x//60%24,x%60)