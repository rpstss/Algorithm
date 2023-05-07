x=int(input())
a=1
sum=0
for i in range(1,x+1):
    sum+=a
    if x<=sum:
        sum-=a
        x-=sum
        if i%2==0:
            print(x,"/",i+1-x,sep="")
            break
        else:
            print(i+1-x,"/",x,sep="")
            break
    a+=1    
        