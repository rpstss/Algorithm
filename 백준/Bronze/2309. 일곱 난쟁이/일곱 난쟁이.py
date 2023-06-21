import itertools

data=[]


for _ in range(9):
    data.append(int(input()))
    
comb=itertools.combinations(data,7)

for i in comb:
    if sum(i)==100:
        result=list(i)
        break
        
result.sort()

for k in result:
    print(k)