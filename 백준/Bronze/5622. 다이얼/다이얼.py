a=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],
   ['W','X','Y','Z']]
l=[]
for i in input():
    for k in a:
        if i in k:
            l.append(a.index(k)+3)
print(sum(l))