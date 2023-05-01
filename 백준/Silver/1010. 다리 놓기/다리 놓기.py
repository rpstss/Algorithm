
import math as m
t=int(input())
for t in range(t):
    n,k=list(map(int,input().split()))
    콤비네이션=m.factorial(k)/(m.factorial(n)*m.factorial(k-n))
    print(int(콤비네이션))
