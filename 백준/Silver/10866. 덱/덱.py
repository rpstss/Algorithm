from collections import deque
import sys
queue=deque()

def func(q):
    if q.startswith("push_front"):
        a,b=q.split()
        queue.appendleft(int(b))
        
    elif q.startswith("push_back"):
        a,b=q.split()
        queue.append(int(b))
        
    elif q=="pop_front":
        if len(queue)==0:
            print(-1)
        else:
            a=queue.popleft()
            print(a)
            
    elif q=="pop_back": 
        if len(queue)==0:
            print(-1)
        else:
            a=queue.pop()
            print(a)
            
    elif q=="size":
        print(len(queue))
        
    elif q=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif q=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
            
n=int(input())
for _ in range(n):
    func(sys.stdin.readline().rstrip())
            