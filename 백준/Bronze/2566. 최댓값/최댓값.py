a=[]
m=[]
for i in range(9):
    l=list(map(int,input().split()))
    a.append(l)
    m.append(max(l))
print(max(m))
print(m.index(max(m))+1,
      a[m.index(max(m))].index(max(a[m.index(max(m))]))+1)