n=input()
a=set()

for i in range(len(n)):
    for k in range(i,len(n)):
        data=n[i:k+1]
        a.add(data)
print(len(a))
