from math import factorial as fa

t=int(input())

for _ in range(t):
    count=0
    data=int(input())
    n_3=data//3
    n_2=data//2
    for i in range(n_3+1):
        for k in range(n_2+1):
            for j in range(data+1):
                result=3*i+2*k+j
                if result==data:
                    count+=int(fa(i+k+j)/(fa(i)*fa(k)*fa(j)))
    print(count)