import sys
input=sys.stdin.readline
data=[]
n=int(input())

for i in range(n):
    a=input().rstrip()
    if len(a)!=1:
        b,c=map(int,a.split())
        data.append(c)
    else:
        a=int(a)
        if a==2:
            if not data:
                print(-1)
            else:
                print(data.pop())
        elif a==3:
            print(len(data))
        elif a==4:
            if data:
                print(0)
            else:
                print(1)
        else:
            if not data:
                print(-1)
            else:
                print(data[-1])
                
