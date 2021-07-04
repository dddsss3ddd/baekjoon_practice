from collections import defaultdict
import sys

wordDic = defaultdict(list)
for _ in range(int(sys.stdin.readline().rstrip())):
    person = sys.stdin.readline().rstrip()
    wordDic[int(person.split(' ')[0])].append(person)

for i in sorted(wordDic.keys()):
    for j in wordDic[i]:
        print(j)
