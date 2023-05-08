N,K=map(int,input().split())
sum=0
for i in range(1,N+1):
    if N%i==0:
        sum+=1
    if sum==K:
        print(i)
        break
if sum<K:
    print(0)