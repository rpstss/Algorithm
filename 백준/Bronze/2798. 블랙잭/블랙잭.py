n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,n-2):
    for k in range(i+1,n-1):
        for j in range(k+1,n):
            b.append(a[i]+a[k]+a[j])
            

for l in b:
    if l <=m:
        c.append(l)
print(max(c))