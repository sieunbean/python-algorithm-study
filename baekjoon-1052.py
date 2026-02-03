def count_ones(n):
    return bin(n).count('1')

N, K = map(int, input().split())

if K == 0:
    print(-1)
    exit()

buy = 0

while count_ones(N) > K:
    N += 1
    buy += 1

print(buy)
