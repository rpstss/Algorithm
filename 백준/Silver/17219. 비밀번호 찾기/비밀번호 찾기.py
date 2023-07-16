import sys
input=sys.stdin.readline
a,b=map(int,input().split())
data={}
for i in range(a):
    c,d=input().split()
    data[c]=d

for k  in range(b):
    print(data[input().rstrip()])
    
