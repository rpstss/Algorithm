import sys
input=sys.stdin.readline
t=int(input())

for i in range(t):
    data=list(map(int,input().split()))
    data.sort()
    print(data[-3])
