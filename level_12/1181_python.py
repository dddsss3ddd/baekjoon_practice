from collections import defaultdict
import sys

wordDic = defaultdict(set)
for _ in range(int(sys.stdin.readline().rstrip())):
    uWord = sys.stdin.readline().rstrip()
    wordDic[len(uWord)].add(uWord)

for i in sorted(wordDic.keys()):
    for j in sorted(wordDic[i]):
        print(j)
