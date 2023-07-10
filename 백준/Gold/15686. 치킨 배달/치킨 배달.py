from itertools import combinations as comb

n,m=map(int,input().split())
home=[]
chicken=[]

for i in range(1,n+1):
    data=list(map(int,input().split()))
    
    for j in range(n):
        if data[j] == 1:
            home.append((i, j + 1))
        elif data[j] == 2:
            chicken.append((i, j + 1))
            
com=comb(chicken,m)

real=[]

for i in com:
    result=[]
    for j in home:
        mins=[]
        for k in i:
            mins.append(abs(j[0]-k[0])+abs(j[1]-k[1]))
        result.append(min(mins))
    real.append(sum(result))
    
print(min(real))