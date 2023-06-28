
def count_k(x):
    sum_k=0
    for i in data:
        count=i-x
        if count>0:
            sum_k+=count
    return sum_k

n,k=map(int,input().split())
data=list(map(int,input().split()))

start=1
end=max(data)

result=0

while start<=end:
    mid=(start+end)//2
    sum_k=count_k(mid)
    
    if sum_k>=k:
        result=mid
        start=mid+1
    else:
        end=mid-1
    
print(result)