t=input()
a=list(map(int,input().split()))
k=0
for i in a:
    num=0
    for j in range(1,i+1):
        if i%j==0:
            num+=1
    if num==2:
        k+=1
        

            
print(k)
            