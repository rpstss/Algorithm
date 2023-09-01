from math import factorial as fac
n,m=map(int,input().split())

print(fac(n)//(fac(m)*fac(n-m)))
