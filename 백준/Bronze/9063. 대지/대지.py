n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
x_1,x_2=min(x),max(x)
y_1,y_2=min(y),max(y)
print(abs(x_1 - x_2)*abs(y_1-y_2))