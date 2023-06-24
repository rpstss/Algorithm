n,k=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(input())
    
for _ in range(k):
    b.append(input())
    
a=set(a)
b=set(b)

c=set(a)&set(b)

c=list(c)
c.sort()
print(len(c))
for i in c:
    print(i)