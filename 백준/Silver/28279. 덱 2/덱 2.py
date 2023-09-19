from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
data=deque()

for i in range(n):
    a=input().rstrip()
    if len(a)==1:
        a=int(a)
        
        if a==3:
            if data:
                print(data.popleft())
            else:
                print(-1)

        elif a==4:
            if data:
                print(data.pop())
            else:
                print(-1)

        elif a==5:
            print(len(data))

        elif a==6:
            if data:
                print(0)
            else:
                print(1)

        elif a==7:
            if data:
                print(data[0])
            else:
                print(-1)

        else:
            if data:
                print(data[-1])
            else:
                print(-1)

    else:
        a=list(map(int,a.split()))

        if a[0]==1:
            data.appendleft(a[1])
        else:
            data.append(a[1])
