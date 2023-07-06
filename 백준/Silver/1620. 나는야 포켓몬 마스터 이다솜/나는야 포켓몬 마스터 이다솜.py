import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dit = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dit[i] = a
    dit[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dit[int(quest)])
    else:
        print(dit[quest])