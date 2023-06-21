import itertools

n,m=map(int,input().split())

data=[i for i in range(1,n+1)]

permu=itertools.permutations(data,m)

for k in permu:
    print(*k)