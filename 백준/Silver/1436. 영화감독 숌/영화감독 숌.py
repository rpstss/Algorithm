n=int(input())
a=[i for i in range(1,2666801)]
b=[k for k in a if "666" in str(k) ]
b=sorted(b)
print(b[n-1])