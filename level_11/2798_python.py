import sys


cardCount,aimNo = map(int,sys.stdin.readline().rstrip().split())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
# cards.sort(reverse=True)
# find = False

def getMaxSum():
    tempbest = 0

    for i in range(len(cards)-2):
        if cards[i] > aimNo:
            continue
        for j in range(i+1,len(cards)-1):
            if cards[i]+cards[j] > aimNo:
                continue
            for k in range(j+1,len(cards)):
                if cards[i]+ cards[j] + cards[k] > aimNo:
                    continue
                elif cards[i]+ cards[j] + cards[k] == aimNo:
                    return aimNo
                elif aimNo-tempbest > aimNo-(cards[i]+cards[j]+cards[k]):
                    tempbest = cards[i]+cards[j]+cards[k]
    return tempbest

print(getMaxSum())