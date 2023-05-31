n=int(input())
for _ in range(n):
    a=input()
    while "()" in a:
        a=a.replace("()","")
    if a=="":
        print("YES")
    else:
        print("NO")