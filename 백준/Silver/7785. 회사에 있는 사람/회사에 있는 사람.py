n=int(input())
data={}
for i in range(n):
    a,b=input().split()
    if b=="enter":
        data[a]=0
        
    else:
        del data[a]
        
result=list(data.keys())
result.sort(reverse=True)

for k in result:
    print(k)