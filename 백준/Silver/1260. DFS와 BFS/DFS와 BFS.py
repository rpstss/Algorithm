import sys
from collections import deque


def bfs(x, N, data,check):
    check[x] = True
    queue = deque()
    queue.append(x)

    while queue:
        pop = queue.popleft()
        print(pop, end=" ")
        for i in data[pop]:
            if  check[i] == False:
                check[i] = True
                queue.append(i)

def dfs(x, N, data, check):

    check[x] = True
    print(x,end=" ")
    
    for i in data[x]:
        if check[i] ==False:
            dfs(i,N,data, check)


N, M, V = map(int,input().split()) # 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
data = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

for j in range(N+1):
    data[j]  = sorted(data[j])
        

    
check = [False]*(N+1)
dfs(V, N, data, check)
print()
check = [False]*(N+1)
bfs(V, N, data,check)


