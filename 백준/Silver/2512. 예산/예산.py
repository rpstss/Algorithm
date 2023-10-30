N = int(input()) # 지방의 수
data = list(map(int,input().split()))
M = int(input()) # 총 예산

def binary_search(start, end, target):
    while start <=end:
        total = 0
        mid = (start+end)//2
        for i in data:
            if i>mid:
                total+=mid
            else:
                total+=i

        if total>target:
            end = mid -1
        else:
            start = mid+1

    return end

result = binary_search(0, max(data), M)
print(result)

