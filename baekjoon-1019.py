N = int(input())
count = [0] * 10

pos = 1
while pos <= N:
    high = N // (pos * 10)
    cur = (N // pos) % 10
    low = N % pos

    for d in range(10):
        if d != 0:
            count[d] += high * pos
            if cur > d:
                count[d] += pos
            elif cur == d:
                count[d] += low + 1
        else:
            if high != 0:
                count[d] += (high - 1) * pos
                if cur > 0:
                    count[d] += pos
                elif cur == 0:
                    count[d] += low + 1

    pos *= 10

print(*count)
