import sys
usrString = list(sys.stdin.readline().rstrip().upper())
alphabetCount = [0]*(ord('z')-ord('a')+1)
resultSet = set()
maxCount = 0
for i in usrString:
    alphabetCount[ord(i)-ord('A')]+=1

    if alphabetCount[ord(i)-ord('A')] > maxCount:
        maxCount = alphabetCount[ord(i)-ord('A')]
        resultSet.clear()
        resultSet.add(i)
    elif alphabetCount[ord(i)-ord('A')] == maxCount:
        resultSet.add(i)

if len(resultSet) > 1:
    print('?')
else:
    print(resultSet.pop())



