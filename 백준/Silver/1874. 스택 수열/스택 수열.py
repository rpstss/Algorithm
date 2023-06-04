count=1
temp=True
stack=[]
result=[]

n= int(input())
for i in range(n):
    a=int(input())
    while count<=a:
        stack.append(count)
        result.append("+")
        count+=1
        
    if stack[-1] !=a:
        temp =False
        break
        
    stack.pop()
    result.append("-")
    
    
        
if temp==False:
    print("NO")
else:
    for i in result:
        print(i)