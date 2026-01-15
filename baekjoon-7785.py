import sys

n = int(sys.stdin.readline())
people = set()

for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        people.add(name)
    else:
        people.remove(name)

for name in sorted(people, reverse=True):
    print(name)
