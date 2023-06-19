N,K=map(int,input().split())
data=[]
count=0

for _ in range(N):
    data.append(int(input()))
    
data.sort(reverse=True)
    
for i in data:
    if K>=i:
        count+=K//i
        K=K%i
        if K==0:
            break
  
print(count)