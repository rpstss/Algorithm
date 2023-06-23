a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e={}

for k in b:
    e[k]=1


for i in range(c):
    if d[i] in e:
        print(1, end=" ")
    else:
        print(0, end=" ")