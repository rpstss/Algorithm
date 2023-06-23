a=[]

while True:
    a=list(input())
    b=list(reversed(a))
    
    if a==["0"]:
        break
    if a==b:
        print("yes")
    else:
        print("no")