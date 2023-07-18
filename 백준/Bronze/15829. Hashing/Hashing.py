n=int(input())
r=31
M=1234567891
data = list(map(lambda x: ord(x) - 96, input()))

result=0
for i in range(n):
    result+=data[i]*(r**i)
    
print(result)
