x=[int(input()) for i in range(3)]
y=set(x)
if sum(x)==180: 
    if y=={60}:
        print("Equilateral")
    elif len(y)==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")