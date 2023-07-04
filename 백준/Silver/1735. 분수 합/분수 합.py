import math
a,b=map(int,input().split())
c,d=map(int,input().split())

a_w=a*d
c_w=c*b

top=a_w+c_w

bottom=b*d

gcd=math.gcd(top,bottom)

print(int(top/gcd),int(bottom/gcd))