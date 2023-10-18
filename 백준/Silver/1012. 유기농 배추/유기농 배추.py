from collections import deque

T = int(input()) # 테스트 케이스



def bfs(x,y):
    
    queue = deque()
    queue.append([x,y])
    while queue:
        a, b = queue.popleft()
        if a-1>=0:
            if data[a-1][b] == 1:
                data[a-1][b] = 0
                queue.append([a-1,b])

        if b-1>=0:
            if data[a][b-1] == 1:
                data[a][b-1] = 0
                queue.append([a,b-1])

        if a+1<=N-1:
            if data[a+1][b] == 1:
                data[a+1][b] = 0
                queue.append([a+1,b])

        if b+1<=M-1:
            if data[a][b+1] == 1:
                data[a][b+1] = 0
                queue.append([a,b+1])
            
    



for i in range(T):
    result = 0
    M, N, K = map(int,input().split()) # 가로, 세로, 위치 개수
    data = [[0]*(M) for _ in range(N)]
    for j in range(K):
        a, b = map(int,input().split())
        data[b][a] = 1

    for c in range(N):
        for d in range(M):
            if data[c][d] == 1:
                bfs(c,d)
                result+=1

    print(result)

    
