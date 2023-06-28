import math
n=int(input())
data=str(math.factorial(n))
result=0
while True:
    if data[-(result+1)]!="0":
        break
    result+=1
    
print(result)