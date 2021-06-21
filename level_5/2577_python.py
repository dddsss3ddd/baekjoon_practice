import sys

valSet = set()
for i in range(10):
  valSet.add(int(sys.stdin.readline().rstrip())%42)

print(len(valSet))
