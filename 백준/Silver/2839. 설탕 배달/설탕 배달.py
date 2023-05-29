n=int(input())
a=[]
for i in range((n//3)+1): # 3키로부터
    for k in range((n//5)+1):
        if i*3+k*5==n:
            a.append(i+k)
            
if a==[]:
    print(-1)
else:
    print(min(a))
            
