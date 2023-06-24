n,k=map(int,input().split())
data=[]
for _ in range(n):
    data.append(int(input()))
    
start=1
end=max(data)

result=0


while start<=end:
    mid=(start+end)//2
    count=0
    for i in data:
        count+=i//mid
    if count>=k:
        start=mid+1
        result=mid
 
    if count<k:
        end=mid-1
        
print(result)