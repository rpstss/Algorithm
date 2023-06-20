n=input()
a=len(n)
result=0
def func(x):
    plus=0
    for i in range(1,x+1):
        plus+=int("9"+"0"*(i-1))*i
    return plus

if a==1:
    print(int(n))
else:
    print(a*(int(n)-int("9"*(a-1)))+func(a-1))
    