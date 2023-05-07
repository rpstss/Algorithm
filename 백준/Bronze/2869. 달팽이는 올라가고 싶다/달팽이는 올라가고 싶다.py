A,B,V=map(int,input().split())
sum=(V-B)/(A-B)
if sum%1!=0:
    print(int(sum)+1)
else:
    print(int(sum))