import sys

N, K = map(int,sys.stdin.readline().rstrip().split())  #  배열 A의 크기, 교환 횟수
data = list(map(int,sys.stdin.readline().rstrip().split()))
count = 0

a = 0
b = 0

for i in range(N):
    for j in range(0, N-i-1):
        if data[j]>data[j+1]:
            count+=1
            data[j+1], data[j] = data[j] , data[j+1]

            if count == K:
                a = data[j+1]
                b = data[j]

if a==0 and b==0:
    print(-1)
else:
    print(b,a)
