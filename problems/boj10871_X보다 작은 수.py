import sys

n,x = map(int,sys.stdin.readline().rstrip().split())
sums = list(map(int,sys.stdin.readline().rstrip().split()))

for i in sums:
    if i<x:
        print(i,end=' ')

#30864	72	Python 3 / 수정	177


# #	29056	56	Python 3	102
# a,b = map(int,input().split())
# score = [x for x in input().split() if int(x)<b]
# print(' '.join(score))