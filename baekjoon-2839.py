N = int(input())

answer = -1

for five in range(N // 5, -1, -1):
    rest = N - five * 5
    if rest % 3 == 0:
        three = rest // 3
        answer = five + three
        break

print(answer)
