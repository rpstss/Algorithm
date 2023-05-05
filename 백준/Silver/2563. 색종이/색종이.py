import sys
n=int(input())
myList=[[0 for k in range(100)]for k in range(100)]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    for j in range(b-1,b+9):
        for h in range(a-1,a+9):
            myList[j][h]=1
sum=0
for i in range(100):
    for j in range(100):
        sum += myList[i][j]
print(sum)