import sys

count = 0
usrin = int(sys.stdin.readline().rstrip())
result = usrin
while True:
    dec = result//10
    uno = result%10
    result = uno*10 + (dec+uno)%10
    count+=1

    if result == usrin:
        break


print(count)
