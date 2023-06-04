n=int(input())
lt=[]
for _ in range(n):
    a,b=input().split()
    a=int(a)
    lt.append([a,b])
lt.sort(key=lambda x:x[0])
for i in lt:
    print(i[0], i[1])
    