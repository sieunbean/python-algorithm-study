N = int(input())
seats = input()

couple = seats.count('LL')

cupholders = N + 1 - couple

print(min(N, cupholders))
