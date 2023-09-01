n=int(input())
a=list(map(int,input().split()))
a_copy=a.copy()
b=list(map(int,input().split()))
b.sort()
a_new=sorted(a)
b_new=[0]*n
result=0


for i in range(n):
    max_index=a.index(a_new[-1-i])
    a[max_index]=101
    b_new[max_index]=b[i]

for k in range(n):
    result+=b_new[k]*a_copy[k]

print(result)

