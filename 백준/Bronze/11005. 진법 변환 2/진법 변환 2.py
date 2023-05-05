N,B=map(int,input().split())
a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=""
while N!=0:
    l+=a[N%B]
    N=N//B
print(l[::-1])