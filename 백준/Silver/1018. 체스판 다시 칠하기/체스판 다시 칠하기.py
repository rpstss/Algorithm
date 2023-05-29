white=["W","B","W","B","W","B","W","B"]
black=["B","W","B","W","B","W","B","W"]
N,M=map(int,input().split()) # N은 행 개수, M은 열 개수
a=[]
for i in range(N):
    a.append(input())
    
c=[]
b=[]
# 흰부터
for i in range(N-7): # 행 8개 남기기

    for k in range(M-7): # 열 8개 남기기
        p=0 #흰
        e=0
        for j in range(i,i+8):
            if j%2==0:
                for q,w in zip(list(a[j][k:k+8]),white):
                    if q!=w:
                        p+=1
                for q,w in zip(list(a[j][k:k+8]),black):
                    if q!=w:
                        e+=1
                        
            else:
                for q,w in zip(list(a[j][k:k+8]),black):
                    if q!=w:
                        p+=1
                for q,w in zip(list(a[j][k:k+8]),white):
                    if q!=w:
                        e+=1
                        
        c.append(p)
        b.append(e)

print(min(min(c),min(b)))
