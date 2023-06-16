t=int(input())
for i in range(t):
    h,w,n=map(int,input().split(" "))
    a=str((n//h)+1) # 뒤 숫자
    b=n%h # 앞 숫자
    if b==0:
        b=h
        a=str(int(a)-1)
    if len(a)==1:
        a="0"+a
    
        
        
  
    print(str(b)+a)