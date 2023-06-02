n=int(input())

for _ in range(n):
    l=[]
    a=input()
    a=a.split("X")
    lt=list(map(len,a))
    for i in lt:
        l.append(int(i*(i+1)/2))
    print(sum(l))