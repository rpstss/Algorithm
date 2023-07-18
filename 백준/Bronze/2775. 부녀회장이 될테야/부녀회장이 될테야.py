import sys
input=sys.stdin.readline

data = [[0] * 14 for _ in range(15)]

data[0]=[i for i in range(1,15)]

for k in range(1,15):
    data[k][0]=data[k-1][0]
    for j in range(1,14):
        data[k][j]=data[k][j-1]+data[k-1][j]

t=int(input())
for i in range(t):
    a=int(input())
    b=int(input())
    print(data[a][b-1])
