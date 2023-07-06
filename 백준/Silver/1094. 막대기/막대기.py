n = int(input())

data= [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(data)):
    if n >= data[i]:
        count += 1
        n -= data[i]

    if n == 0:
        break

print(count)