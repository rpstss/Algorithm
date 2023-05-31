from collections import deque
import sys

queue = deque()
n = int(input())

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    
    if a.startswith("pu"):
        a = a.split()
        queue.append(int(a[1]))
    elif a.startswith("po"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif a.startswith("si"):
        print(len(queue))
    elif a.startswith("e"):
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a.startswith("f"):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
