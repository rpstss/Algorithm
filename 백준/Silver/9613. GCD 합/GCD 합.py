import itertools
import math
result=[]
n=int(input())
for _ in range(n):
    a=[]
    l=list(map(int,input().split()))
    del l[0]
    comb=list(itertools.combinations(l,2))
    for k,j in comb:
        a.append(math.gcd(k,j))
    result.append(sum(a))
    
for i in result:
    print(i)
    