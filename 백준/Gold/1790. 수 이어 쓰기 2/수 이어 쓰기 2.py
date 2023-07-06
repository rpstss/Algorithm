n, k = map(int, input().split())
a = 0
digit = 1
b = 9


while k > digit*b:
    k = k-(digit * b)
    a = a + b
    digit+=1
    b = b*10

a = (a+1) + (k-1) // digit

if a > n:
    print(-1)
else:
    print(str(a)[(k-1)%digit])