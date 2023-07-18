n=int(input())
data=list(map(int,input().split()))
data.sort()

result=[0]*n

result[0]=data[0]

for i in range(1,n):
    result[i]=result[i-1]+data[i]
    
print(sum(result))