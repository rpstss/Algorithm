a=[]
for i in range(5):
    a.append(list(input()))
a_0=len(a[0])
a_1=len(a[1])
a_2=len(a[2])
a_3=len(a[3])
a_4=len(a[4])
m=max(list([a_0,a_1,a_2,a_3,a_4]))
s=""
for k in range(1,m+1):
    if a_0>=k:
        s+=a[0][k-1]
    if a_1>=k:
        s+=a[1][k-1]
    if a_2>=k:
        s+=a[2][k-1]
    if a_3>=k:
        s+=a[3][k-1]
    if a_4>=k:
        s+=a[4][k-1]

print(s)

