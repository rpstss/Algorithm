from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    count=0
    queue=deque()
    a,b=map(int,input().split()) # 문서 개수, 몇 번째를 찾는지
    c=list(map(int,input().split()))
    for k in range(a):
        queue.append((c[k],k))
    result=queue[b]
    c.sort()
    while True:
        if c[-1]==queue[0][0]:
            d=queue.popleft()
            count+=1
            c.pop()
            if d==result:
                break
        else:
            queue.append(queue.popleft())
    print(count)

