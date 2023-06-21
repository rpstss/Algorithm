import itertools

n,m=map(int,input().split())

data=[i for i in range(1,n+1)]

comb=list(itertools.combinations(data,m))

for k in comb:
    print(*k)