N,B=input().split()
B=int(B)
a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myList=[a.index(x) for x in N]
l=len(N)
sum=0
for i in range(len(N)):
    sum+=myList[i]*B**(l-1)
    l-=1
print(sum)
    
    