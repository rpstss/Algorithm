from math import factorial as fa

n,k=map(int,input().split())

print(int(fa(n)/(fa(k)*fa(n-k))))