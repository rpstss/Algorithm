n,m=map(int,input().split())
for i in range(n,m+1):
    result=True
    if i==1:
        continue
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            result=False
            break
    if result:
        print(i)