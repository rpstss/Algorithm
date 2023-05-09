x=[]
y=[]
result=[]
for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
s_1=list(set(x))
s_2=list(set(y))

if x.count(s_1[0])==2:
    result.append(s_1[1])
else:
    result.append(s_1[0])

    
if y.count(s_2[0])==2:
    result.append(s_2[1])
else:
    result.append(s_2[0])
    

print(*result)