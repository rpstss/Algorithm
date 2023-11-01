import sys

N, K = map(int,sys.stdin.readline().rstrip().split())  #  배열 A의 크기, 교환 횟수
data = list(map(int,sys.stdin.readline().rstrip().split()))
count = 0

a = 0


for i in range(1,N):
    key = data[i]
    j = i-1
    if key >= data[j]:
        continue
    while j>=0 and key<data[j]:
        data[j+1]= data[j]
        
        count+=1
        if count == K:
            a=data[j]
        j-=1
    data[j+1] = key
    count+=1
    if count == K:
            a=data[j]

if a==0:
    print(-1)
else:
    print(a)


    
