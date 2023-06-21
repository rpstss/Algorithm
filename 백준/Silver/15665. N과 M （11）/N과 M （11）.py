import itertools

n,m=map(int,input().split())

data=list(set(list(map(int,input().split()))))


perm=list(itertools.product(data,repeat=m))

perm.sort()

for k in perm:
    print(*k)