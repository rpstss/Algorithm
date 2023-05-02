num=int(input())
sum=0
for i in range(num):
  check=[]
  word=input()
  for k in set(word):
    count=word.count(k)
    if k*count in word:
      check.append(0)
    else:
      check.append(1)
  if 1 not in check:
    sum+=1
  
print(sum)