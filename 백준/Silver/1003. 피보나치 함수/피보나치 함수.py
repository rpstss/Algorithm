t=int(input())

for _ in range(t):
    data_0=[1,0]
    data_1=[0,1]
    n=int(input())
    if n>1:
        for i in range(n-1):
            data_0.append(data_1[-1])
            data_1.append(data_0[-2]+data_1[-1])

    print(data_0[n], data_1[n])
    