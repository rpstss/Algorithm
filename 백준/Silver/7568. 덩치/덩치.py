n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

for k in data: # 비교할 값
    count=0
    for j in data: # 비교당할 값
        if j[0]>k[0] and j[1]>k[1]:
            count+=1
    print(count+1,end=" ")
        
    
