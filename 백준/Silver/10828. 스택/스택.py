import sys
a=[]
def push(x):
    a.append(x)

def pop():
    if len(a)==0:
        print(-1)
    else:
        print(a[-1])
        del a[-1]
    
def size():
    print(len(a))
    
def empty():
    if len(a)==0:
        print(1)
    else:
        print(0)

def top():
    if len(a)==0:
        print(-1)
    else:
        print(a[-1])
        
N = int(sys.stdin.readline().rstrip())


for _ in range(N):
    x = sys.stdin.readline().rstrip()
    if " " in x:
        push(int(x[x.index(" ")+1::]))
    else:
        if x=="pop":
            pop()
        elif x=="size":
            size()
        elif x=="empty":
            empty()
        else:
            top()
            
        