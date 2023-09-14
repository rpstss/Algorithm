data=[]
for i in range(8):
    data.append((i+1,int(input())))

data.sort(key=lambda x: x[1])

data=data[-5::]
a=[]
b=[]
for i in range(5):
    a.append(data[i][0])
    b.append(data[i][1])

print(sum(b))
a.sort()
print(*a)
    
