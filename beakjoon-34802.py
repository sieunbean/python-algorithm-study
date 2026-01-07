a = input()
b = input()
t, k = map(int, input().split())

h, m, s = map(int, a.split(':'))
now = h * 3600 + m * 60 + s

h, m, s = map(int, b.split(':'))
start = h * 3600 + m * 60 + s

run = t * (100 - k) // 100

if now + run <= start:
    print(1)
else:
    print(0)

