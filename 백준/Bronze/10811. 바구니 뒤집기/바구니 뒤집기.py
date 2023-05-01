n,m=map(int,input().split())
x=list(range(1,n+1))
for k in range (m):
    i,j=map(int,input().split())
    x[i-1:j]=list(reversed(x[i-1:j]))
for i in x:
    print(i, end=" ")
    