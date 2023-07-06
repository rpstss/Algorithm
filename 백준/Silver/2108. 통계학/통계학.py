import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]

print(round(sum(data) / n))
data = sorted(data)
print(data[n // 2])

counter = Counter(data)
m = max(counter.values())
b = [k for k, v in counter.items() if v == m]
b.sort()

if len(b) >= 2:
    print(b[1])
else:
    print(b[0])

print(data[-1] - data[0])
