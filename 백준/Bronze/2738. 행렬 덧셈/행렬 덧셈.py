N,M=map(int, input().split())
A=[]
B=[]
for i in range(N):
    a=list(map(int,input().split()))
    A.append(list(a))
for i in range(N):
    a=list(map(int,input().split()))
    c=list((A[i][k]+a[k]) for k in range(M))
    B.append(c)
for j in range(N):
    print(" ".join(map(str,B[j])))