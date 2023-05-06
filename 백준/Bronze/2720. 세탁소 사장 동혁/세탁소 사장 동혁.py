T=int(input())
for i in range(T):
    charge=[]
    pay=int(input())
    charge.append(pay//25)
    pay%=25
    charge.append(pay//10)
    pay%=10
    charge.append(pay//5)
    pay%=5
    charge.append(pay)
    print(*charge)