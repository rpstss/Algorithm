# 나의 코드
d=[0]*(10**6+1)

n=int(input())

for i in range(2,n+1):
    result=[]
    if i%3==0:
        result.append(d[i//3])
    if i%2==0:
        result.append(d[i//2])
    result.append(d[i-1])
    
    result_min=min(result)
    d[i]=result_min+1
    
print(d[n])
    