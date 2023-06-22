n=int(input())
data=[]
for i in range(n):
    data.append(input())
    
data=list(set(data))    
data.sort(key=lambda x: (len(x), x))

for k in data:
    print(k)