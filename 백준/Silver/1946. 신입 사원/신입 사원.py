import sys

t = int(input())

for _ in range(t):
    test=int(input())
    rank=[list(map(int, sys.stdin.readline().split())) for _ in range(test)]
    rank.sort()
    result= 1
    k=0
    
    for i in range(1,test):
        if rank[i][1] < rank[k][1]:
            result += 1
            k=i
    
    print(result)