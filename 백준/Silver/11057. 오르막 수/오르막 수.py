from math import factorial as fa

n = int(input())
result = int(fa(9 + n) // (fa(n) * fa(9)) % 10007)
print(result)
