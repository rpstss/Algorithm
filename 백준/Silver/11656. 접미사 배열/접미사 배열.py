from collections import deque

queue=deque(input())

result=[]

for i in range(len(queue)):
    result.append(list(queue))
    queue.popleft()
    
result_str=list(map("".join, result))
result_str.sort()

for k in result_str:
    print(k)