word=input()
sum=0
for i in ["c=",'c-','dz=','d-','lj','nj','s=','z=']:
    if i in word:
        sum+=word.count(i)
    word=word.replace(i," ")
word=word.replace(" ","")
sum+=len(word)
print(sum)