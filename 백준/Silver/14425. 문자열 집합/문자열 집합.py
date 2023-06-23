import sys
n,m=map(int,sys.stdin.readline().split())

dic={}

for i in range(n):
    dic[sys.stdin.readline().rstrip()]=0
    
for k in range(m):
    a=sys.stdin.readline().rstrip()
    if a in dic:
        dic[a]+=1
    
print(sum(dic.values()))