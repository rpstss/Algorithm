data=[0]*101
data[1]=1
data[2]=1
data[3]=1

def fun(x):
  if data[x]==0:
    data[x]=fun(x-2)+fun(x-3)
  return data[x]


t=int(input())

for i in range(t):
  print(fun(int(input())))