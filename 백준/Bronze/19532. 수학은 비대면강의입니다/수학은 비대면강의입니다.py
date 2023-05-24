a=list(map(int, input().split()))

for i in range(-999,1000):
    for k in range(-999,1000):
        if a[0]*i +a[1]*k==a[2] and a[3]*i + a[4]*k == a[5]:
            print(i,k)