import sys
while True:
    a=list(map(int,input().split()))
    a.sort()
    if a==[0,0,0]:
        break
    elif a[2]<a[1]+a[0]:
        if len(set(a))==1:
            print("Equilateral")
        elif len(set(a))==2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")