while True:
    t=int(input())
    if t==-1:
        break
    a=[]
    
    for i in range(1,t):
        if t%i==0:
            a.append(str(i))
    
    if sum(list(map(int,a)))==t:
        print(t,"=",end=" ")
        print(" + ".join(a))
    else:
        print(t,"is NOT perfect.")