n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    N=a[0]
    l=a[1:]
    mean=sum(l)/len(l)
    por=len(list(k for k in l if k > mean))/len(l)*100
    print("%.3f"%por,"%",sep="")
    
