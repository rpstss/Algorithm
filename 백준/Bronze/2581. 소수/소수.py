M=int(input())
N=int(input())
sum_decimal=[]
for i in range(M,N+1):
    for k in range(2,i+1):
        if i%k==0:
            if k==i:
                sum_decimal.append(i)
            break
if len(sum_decimal)==0:
    print(-1)
else:
    print(sum(sum_decimal))
    print(min(sum_decimal))