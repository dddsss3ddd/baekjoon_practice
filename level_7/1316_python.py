import sys
usrCount = int(sys.stdin.readline().rstrip())
res = 0
for i in range(usrCount):
    charSet = set()
    lastChar = ''
    isGroup = True

    usrWord = list(sys.stdin.readline().rstrip())
    for x in usrWord:
        if x == lastChar:
            continue
        else:
            lastChar = x
            if x in charSet:
                isGroup = False
                break
            else:
                charSet.add(x)
        if not isGroup:
            break
    if isGroup:
        res+=1

print(res)

# result = 0
# for i in range(int(input())):
#     word = input()
#     print(word.find(word))
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)
