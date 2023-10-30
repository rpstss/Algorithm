import sys
from collections import deque

N, M = map(int,input().split())  #  정점의 개수, 간선의 개수

data = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    a, b =map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

def bfs(x):
    visited[x] = True
    queue = deque()
    queue.append(x)
    
    while queue:
        pop = queue.popleft()
        for i in data[pop]:
            if not visited[i]  :
                visited[i] =True
                queue.append(i)

    
result = 0

for j in range(1, N+1):
    if not visited[j]:
        bfs(j)
        result+=1

print(result)
