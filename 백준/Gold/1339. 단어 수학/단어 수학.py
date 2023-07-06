import collections
n = int(input())
data=[]
q=collections.defaultdict(int)
for _ in range(n):
    a=input()
    for i in range(len(a)):
        q[a[i]]+=(10**(len(a)-i-1))
    data.append(a)
q=list(sorted(q.items(), key=lambda f:-f[1]))
answer=0
for i in range(9,9-len(q),-1):
    answer+=q[9-i][1]*i
print(answer)