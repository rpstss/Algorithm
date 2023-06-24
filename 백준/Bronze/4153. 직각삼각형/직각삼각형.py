while True:
    data=list(map(int,input().split()))
    if data==[0,0,0]:
        break
    M=max(data)
    data.remove(M)
    if M**2==data[0]**2+data[1]**2:
        print('right')
    else:
        print('wrong')