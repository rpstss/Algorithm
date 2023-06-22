s=input()
n=ord("z")-ord("a")+1
result=[]
for i in range(n):
    result.append(s.count(chr(ord("a")+i)))
    
print(*result)