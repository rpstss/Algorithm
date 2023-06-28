n,k=map(int,input().split())
data=[i for i in range(1,n+1)]

a=0

result=[]

while True:
    if data==[]:
        break
    a = (a + k - 1) % len(data)
    result.append(data.pop(a))
        
result=", ".join(map(str,result))
result="<"+result+">"
print(result)