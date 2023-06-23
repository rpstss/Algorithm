import sys
n=int(input())

array=[0]*100001

for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    array[a]+=1
    
for k in range(len(array)):
    for j in range(array[k]):
        print(k)