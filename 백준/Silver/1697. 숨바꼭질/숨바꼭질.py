from collections import deque
n,k=map(int,input().split())

def bfs():
    queue=deque()
    queue.append(n)
    graph[n]==1
    while len(queue)!=0:
        a=queue.popleft()
        
        if a==k:
            return graph[a]
        
        for i in [a-1,a+1,a*2]:
            if i<0 or i>=100001 or graph[i]!=0:
                continue
            queue.append(i)
            graph[i]=graph[a]+1
                

graph=[0]*100001

print(bfs())