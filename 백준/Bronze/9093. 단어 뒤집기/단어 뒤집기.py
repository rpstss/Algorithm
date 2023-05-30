T = int(input())

for _ in range(T):
    a = input()
    b = ""
    if a.count(" ") == 0:
        print(a[::-1])
    else:
        words = a.split()
        for word in words:
            b += "".join(reversed(word)) + " "
        print(b.rstrip())
