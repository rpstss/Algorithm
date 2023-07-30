import sys
input=sys.stdin.readline

m=int(input().rstrip())
s=set()
for _ in range(m):
    k=input().rstrip()
    if k=="all":
        s=set( i for i in range(1,21))
    elif k=="empty":
        s=set()
    else:
        a,b=k.split()
        b=int(b)
   

        if a=="add":
            s.add(b)
        elif a=="remove":
            s.discard(b)
        elif a=="check":
            if b in s:
                print(1)
            else:
                print(0)
        elif a=="toggle":
            if b in s:
                s.discard(b)
            else:
                s.add(b)



                