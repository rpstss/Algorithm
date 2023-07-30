import sys
input = sys.stdin.readline

n,m=map(int,input().split())
judge=[0 for j in range(n)]

data=list(map(int,input().split()))
judge[0]=data[0]
for i in range(1,n):
    judge[i]=judge[i-1]+data[i]

judge=[0]+judge
for i in range(m):
    a,b=map(int,input().split())

    print(judge[b]-judge[a-1])