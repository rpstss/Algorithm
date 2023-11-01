import sys

N, K = map(int,sys.stdin.readline().rstrip().split())  #  배열 A의 크기, 교환 횟수
data = list(map(int,sys.stdin.readline().rstrip().split()))
count = 0

a = 0
b = 0

for i in range(N-1, 0, -1):
    max_index = i
   
    for j in range( i+1):
        if data[j] > data[max_index]:
            max_index = j
            
    if max_index != i:
        count+=1
        data[max_index], data[i] = data[i], data[max_index]
        
    if count == K:
        a=data[max_index]
        b=data[i]
    

if a==0 and b==0:
    print(-1)
else:
    print(a, b)
