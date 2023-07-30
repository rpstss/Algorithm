t=int(input())

for i in range(t):
    data={}
    result=1
    k=int(input())
    for j in range(k):
        a,b=input().split()
        if b in data:
            data[b]+=1
        else:
            data[b]=1
    for q in data.values():
        result*=(q+1)
    print(result-1)
