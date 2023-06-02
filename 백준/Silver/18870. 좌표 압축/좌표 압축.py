n=int(input())
lt=list(map(int,input().split()))

lt_set=list(set(lt))
lt_set.sort()

index={}
index_count=0
for i in lt_set:
    index[i]=index_count
    index_count+=1

for i in lt:
    print(index[i],end=" ")