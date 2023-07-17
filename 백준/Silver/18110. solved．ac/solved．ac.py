import sys

input=sys.stdin.readline

def fun(x):
    judge = x - int(x)
    if judge >= 0.5:
        x = int(x) + 1
    else:
        x = int(x)
    return x

n = int(input())
data = []

if n == 0:
    print(0)
else:
    for i in range(n):
        data.append(int(input()))

    data.sort()

    num_of_remove = fun(n * 0.15)
    data = data[num_of_remove:n-num_of_remove]

    if len(data) == 0:
        print(0)
    else:
        result = fun(sum(data) / len(data))
        print(result)
