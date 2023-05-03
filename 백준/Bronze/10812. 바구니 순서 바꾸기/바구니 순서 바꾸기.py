N,M=map(int, input().split())
box=[k+1 for k in range(N)]
for a in range(M):
    i,j,k=map(int, input().split())
    box[i-1:j]=box[k-1:j]+box[i-1:k-1]
for b in box:
    print(b, end=" ")