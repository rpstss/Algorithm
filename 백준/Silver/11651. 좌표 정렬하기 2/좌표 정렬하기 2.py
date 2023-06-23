import sys

array=[]

n=int(sys.stdin.readline())

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    array.append((a,b))
    
array.sort(key=lambda x:(x[1],x[0]))

for k in array:
    print(k[0],k[1])
    