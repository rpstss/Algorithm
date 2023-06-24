n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i in dic:
        dic[i]+=1
        
    else:
        dic[i]=1
        
m=int(input())
data_2=list(map(int,input().split()))

for k in data_2:
    if k in dic:
        print(dic[k],end=" ")
    else:
        print(0,end=" ")