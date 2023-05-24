n=int(input())
for i in range(n+1):
    a=list(map(int,str(i)))
    sum_=sum(a)+i
    if sum_==n:
        print(i)
        break
    if n==i:
        print(0)