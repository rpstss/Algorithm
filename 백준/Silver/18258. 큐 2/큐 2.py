from collections import deque
import sys

N = int(input())

queue = deque()
def empty():
    if not queue:
        print(1)
    else:
        print(0)
        
def push(x):
    queue.append(x)

def pop():
    if not queue:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()

def size():
    print(len(queue))

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])

for i in range(N):
    action = sys.stdin.readline().rstrip()

    if action == "pop":
        pop()
    elif action =="size":
        size()
    elif action=="empty":
        empty()
    elif action == "front":
        front()
    elif action=="back":
        back()
    else:
        push(int(action.split()[1]))
